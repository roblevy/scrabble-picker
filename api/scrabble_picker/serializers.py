from rest_framework import serializers

from api.scrabble_picker.models import Game


class GameSerializer(serializers.ModelSerializer):

    class Meta:
        model = Game
        read_only_fields = fields = ['game_code', 'letters_remaining']
