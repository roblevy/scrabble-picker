from uuid import uuid4

from rest_framework import viewsets

from scrabble_picker.play.models import Game
from scrabble_picker.play.serializers import GameSerializer


class GameViewSet(viewsets.ModelViewSet):
    queryset = Game.objects.all().order_by('game_code')
    serializer_class = GameSerializer


def games_create():
    game_code = uuid4().hex[:4]
    game = Game(game_code=game_code)
    game.save()
    return game_code
