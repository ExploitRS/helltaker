from enum import Enum
from copy import deepcopy

import pyxel

class Position:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Position(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Position(self.x - other.x, self.y - other.y)

    def __iadd__(self, other):
        self = self + other
        return self

    def __eq__(self, other) -> bool:
        if (self.x == other.x) and (self.y == other.y):
            return True

    def to_str(self):
        return f"x: {self.x}\ny: {self.y}"
        
    def render_as_text(self):
        pyxel.text(10, 30, self.to_str(), 7)

class Direction(Enum):
    Right = Position(8, 0)
    Left  = Position(-8, 0)
    Up    = Position(0, -8)
    Down  = Position(0, 8)



class Avatar:
    def __init__(self, x, y, img, u, v, w, h, col):
        self._pos_       = Position(x, y)
        self._start_pos_ = Position(x, y)
        self._img_       = img
        self._u_         = u
        self._v_         = v
        self._w_         = w
        self._h_         = h
        self._col_       = col

    def update(self):
        pass

    def draw(self):
        pyxel.blt(
            self._pos_.x,
            self._pos_.y,
            self._img_,
            self._u_,
            self._v_,
            self._w_,
            self._h_,
            self._col_,
        )

    def render_position(self):
        self._pos_.render_as_text()

    def move(self, pos: Position):
        self._pos_ = pos

    def neighbor(self, dir: Direction) -> Position:
        pos = deepcopy(self._pos_)
        dir_pos = dir.value
        pos += dir_pos
        return pos

    def reset_pos(self):
        self._pos_ = self._start_pos_

    def pos(self) -> Position:
        return self._pos_
