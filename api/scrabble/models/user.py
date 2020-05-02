from dataclasses import dataclass
from uuid import uuid4


@dataclass
class User:
    id: str
    name: str

    def __init__(self, name):
        self.id = uuid4().hex
        self.name = name
