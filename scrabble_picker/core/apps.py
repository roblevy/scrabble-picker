from django.apps import AppConfig
from pathlib import Path


class ScrabblePicker(AppConfig):
    name = 'scrabble_picker.core'

    def ready(self):
        Path("/tmp/app-initialized").touch()
