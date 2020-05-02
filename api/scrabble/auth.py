import json
import uuid
from functools import wraps
from pathlib import Path

from flask import request
from sqlitedict import SqliteDict
from models.user import User

HERE = Path(__file__).parent
USERS = SqliteDict(HERE / 'users_object_store.sqlite', autocommit=True)


def str_uuid() -> str:
    return uuid.uuid4().hex


def create_user():
    if request.json:
        if username := request.json.get('name'):
            user = User(name=username)
            USERS[user.id] = user
            return user


def get_user_from_request():
    if request.json:
        if userid := request.json.get('userid'):
            return USERS.get(userid)


def check_user(fun):
    @wraps(fun)
    def _check_user(*args, **kwargs):
        if user := get_user_from_request():
            return fun(*args, **kwargs, user=user)
        msg = json.dumps('Unauthorized')
        return msg, 401
    return _check_user
