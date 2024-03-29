from rest_framework import viewsets
import random
from rest_framework.decorators import action

from scrabble_picker.core.models import Game
from scrabble_picker.core.serializers import GameSerializer
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.renderers import StaticHTMLRenderer
from django.http import HttpResponse


class GameViewSet(viewsets.ModelViewSet):
    queryset = Game.objects.all()
    serializer_class = GameSerializer

    @action(detail=True, methods=["get", "post"])
    def draw(self, request, *args, **kwargs):
        """
        Draw `letters_count` letters from the bag
        """
        game = self.get_object()
        drawn_letters = []
        for i in range(request.data["count"]):
            letters_remaining = game.letters_remaining
            drawn_letter = random.choice(letters_remaining)
            game.letters_remaining = letters_remaining.replace(drawn_letter, "", 1)
            drawn_letters.append(drawn_letter)
        game.save()
        return Response(
            {"game": GameSerializer(game).data, "letters_drawn": drawn_letters}
        )
