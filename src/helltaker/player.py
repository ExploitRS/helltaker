from enum import Enum
import pyxel

class Player:
    def __init__(self):
        self._x_ = 72
        self._y_ = 32
        self._direction_ = None

    def draw(self):
        pyxel.blt(
            self._x_,
            self._y_,
            0,
            8,
            0,
            16,
            8,
            12,
        )

class Direction(Enum):
    Right = 1
    Left  = 2
    Up    = 3
    Down  = 4