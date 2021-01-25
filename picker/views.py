from uuid import uuid4

from rest_framework import viewsets

from .models import Game
from .serializers import GameSerializer


class GameViewSet(viewsets.ModelViewSet):
    queryset = Game.objects.all().order_by('game_code')
    serializer_class = GameSerializer


def games_create():
    game_code = uuid4().hex[:4]
    game = Game(game_code=game_code)
    game.save()
    return game_code
