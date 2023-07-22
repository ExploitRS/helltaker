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
    def neighbor(self, dir: Direction) -> Position:
        pos = deepcopy(self._pos_)
        dir_pos = dir.value
        pos += dir_pos
        return pos
