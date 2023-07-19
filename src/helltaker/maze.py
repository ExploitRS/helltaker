from enum import Enum

import pyxel

import conf

class Maze:
    def __init__(self, tm: TileMap, start_pos,end_pos, enemies):
        self._tilemap_ = tm
        self._is_clear = False
        self._start_pos_ = start_pos
        self._end_pos = end_pos
        self._enemy_pos_list_ = enemy_pos_list
 
    def update(self):
        pass

    def draw(self):
        pyxel.bltm((self._x_ / 2) - (self._w_ / 2), (self._y_ / 2) - (self._h_ / 2), self._tm_, self._u_, self._v_, self._w_, self._h_)

# For pyxel purpose
class TileMap:
    def __init__(self, x, y, tm, u, v, w, h, col):
        self._x_   = x
        self._y_   = y
        self._tm_  = tm
        self._u_   = u
        self._v_   = v
        self._w_   = w
        self._h_   = h
        self._col_ = col


class Tile:
    def __init__(self, x, y, tile_kind):
        self._x_ = x
        self._y_ = y
        self._kind_: TileKind = tile_kind

class TileKind(Enum):
    Floor = 0
    Wall = 1
