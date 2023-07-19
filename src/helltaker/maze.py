from enum import Enum

import pyxel

import conf

class Maze:
    def __init__(self, conf: conf.Conf, tm, u, v, w, h, col):
        self._x_   = conf._x_
        self._y_   = conf._y_
        self._tm_  = tm
        self._u_   = u
        self._v_   = v
        self._w_   = w
        self._h_   = h
        self._col_ = col

    def update(self):
        pass

    def draw(self):
        pyxel.bltm((self._x_ / 2) - 28, (self._y_ / 2) - 24, self._tm_, self._u_, self._v_, self._w_, self._h_)

class Tile:
    def __init__(self, x, y, tile_kind):
        self._x_ = x
        self._y_ = y
        self._kind_: TileKind = tile_kind

class TileKind(Enum):
    Floor = 0
    Wall = 1
