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
    '*': 2
}

ALL_LETTERS = ''.join(k * v for k, v in LETTER_COUNTS.items())

class Game(models.Model):
    game_code = models.CharField(max_length=5)
    letters_drawn = models.CharField(default='', max_length=len(ALL_LETTERS))
