import json
from pathlib import Path

from flask import Flask
from flask_cors import CORS
from sqlitedict import SqliteDict

from scrabble.auth import check_user, create_user
from scrabble.dataclasses_json import json_dump_class
from scrabble.models.game import Game

HERE = Path(__file__).parent

app = Flask(__name__)
CORS(app)


GAMES = SqliteDict(HERE / 'games_object_store.sqlite', autocommit=True)


@app.route('/')
def hello_world():
    return 'Welcome to the Scrabble Picker API'


@app.route('/users', methods=['POST'])
def users_create():
    if user := create_user():
        res = {
            "user": user
        }
        return json_dump_class(res)
    msg = json.dumps('No user created')
    return msg, 400

@app.route('/games', methods=['POST'])
@check_user
def games_create(user):
    """
    Games CREATE - returns Game
    """
    game = Game(created_by=user)
    GAMES[game.code] = game
    res = {
        "game": game
    }
    return json_dump_class(res)
