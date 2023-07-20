from enum import Enum
from copy import deepcopy

import pyxel

from avatar import Avatar, Position

class Direction(Enum):
    Right = Position(8, 0)
    Left  = Position(-8, 0)
    Up    = Position(0, -8)
    Down  = Position(0, 8)

class Player(Avatar):
    def update(self):
        pass

    def neighbor(self, dir: Direction) -> Position:
        pos = deepcopy(self._pos_)
        print(f"x: {pos.x}")
        print(f"y: {pos.y}")
        dir_pos = dir.value
        print(f"dirx: {dir_pos.x}")
        pos.sub_update(dir_pos.x, dir_pos.y)
        print(f"neix {pos.x}")
        print(f"neiy {pos.y}")
        print(f"naita: {self._pos_.x}")
        return pos

    def move(self, pos: Position):
        print(f"move: {pos.x}")
        self._pos_ = pos
