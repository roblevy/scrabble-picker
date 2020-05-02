from dataclasses import dataclass
from datetime import datetime
from typing import List, Union
from uuid import UUID
from uuid import uuid4
from models.user import User


@dataclass
class Game:
    code: str
    participants: List[User]
    letter_pool: List[str]
    turn_indicator: int
    game_started_at: Union[None, datetime]

    def __init__(self, created_by: User):
        self.code = uuid4().hex
        self.participants = [created_by]
        self.letter_pool = 'ABC'
        self.turn_indicator = 0
        self.game_started_at = None
