from rest_framework import serializers

from api.scrabble_picker.models import Game
from uuid import uuid4


class GameSerializer(serializers.ModelSerializer):

    class Meta:
        model = Game
        fields = ['game_code', 'letters_remaining']
        read_only_fields = ['game_code', 'letters_remaining']

    def create(self, validated_data):
        game_code = uuid4().hex[:4]
        game = Game(game_code=game_code)
        game.save()
        return game
