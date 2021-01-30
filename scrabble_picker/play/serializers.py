from rest_framework import serializers

from scrabble_picker.play.models import Game


class GameSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Game
        fields = ('game_code', )
