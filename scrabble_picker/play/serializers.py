from rest_framework import serializers

from scrabble_picker.play.models import Game
from uuid import uuid4


class GameSerializer(serializers.HyperlinkedModelSerializer):
    model = Game
    fields = {"game_code": serializers.CharField(max_length=5)}

    def create(self):
        game_code = uuid4().hex[:4]
        return Game.objects.create(game_code=game_code)
