import random
import uuid
from typing import Dict

from django.db import models

LETTER_COUNTS = {
    'a': 9,
    'b': 2,
    'c': 2,
    'd': 4,
    'e': 12,
    'f': 2,
    'g': 3,
    'h': 2,
    'i': 9,
    'j': 1,
    'k': 1,
    'l': 4,
    'm': 2,
    'n': 6,
    'o': 8,
    'p': 2,
    'q': 1,
    'r': 6,
    's': 4,
    't': 6,
    'u': 4,
    'v': 2,
    'w': 2,
    'x': 1,
    'y': 2,
    'z': 1,
    '*': 2,
}


def letter_string(letter_counts: Dict[str, int]) -> str:
    return ''.join(k * v for k, v in letter_counts.items())


ALL_LETTERS = letter_string(LETTER_COUNTS)


def create_game_code() -> str:
    return uuid.uuid4().hex[:5]


class Game(models.Model):
    game_code = models.CharField(max_length=5, primary_key=True, default=create_game_code)
    letters_remaining = models.CharField(default=ALL_LETTERS, max_length=len(ALL_LETTERS))
