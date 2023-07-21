from enum import Enum
from copy import deepcopy

import pyxel

import conf
from player import Player, Direction
from enemy import Enemy
from avatar import Position

class Maze:
    def __init__(self, tm, steps, player: Player, enemies: list[Enemy], end_pos, walls):
        self._tilemap_  = tm
        self._is_clear_ = False
        self._steps_    = steps
        self._max_steps_ = steps
        self._player_   = player 
        self._srt_pos_  = player._pos_
        self._enemies_  = enemies
        self._end_pos_  = end_pos
        self._walls_    = walls
 
    def update(self):
        if 0 >= self._steps_:
            self._player_._pos_ = self._srt_pos_
            self._steps_ = self._max_steps_

        if pyxel.btnp(pyxel.KEY_LEFT) or pyxel.btnp(pyxel.GAMEPAD1_BUTTON_DPAD_LEFT) or pyxel.btnp(pyxel.KEY_A):
            dir = Direction.Left
            neighbor = self._player_.neighbor(dir)
            if neighbor not in self._walls_:
                self._player_.move(neighbor)
                self._steps_ -= 1

            else:
                self._player_.move(self._player_._pos_)

        if pyxel.btnp(pyxel.KEY_RIGHT) or pyxel.btnp(pyxel.GAMEPAD1_BUTTON_DPAD_RIGHT) or pyxel.btnp(pyxel.KEY_D):
            dir = Direction.Right
            neighbor = self._player_.neighbor(dir)

            if neighbor not in self._walls_:
                self._player_.move(neighbor)
                self._steps_ -= 1

            else:
                self._player_.move(self._player_._pos_)

        if pyxel.btnp(pyxel.KEY_UP) or pyxel.btnp(pyxel.GAMEPAD1_BUTTON_DPAD_UP) or pyxel.btnp(pyxel.KEY_W):
            dir = Direction.Up
            neighbor = self._player_.neighbor(dir)
            if neighbor not in self._walls_:
                self._player_.move(neighbor)
                self._steps_ -= 1

            else:
                self._player_.move(self._player_._pos_)

        if pyxel.btnp(pyxel.KEY_DOWN) or pyxel.btnp(pyxel.GAMEPAD1_BUTTON_DPAD_DOWN) or pyxel.btnp(pyxel.KEY_S):
            dir = Direction.Down
            neighbor = self._player_.neighbor(dir)
            if neighbor not in self._walls_:
                self._player_.move(neighbor)
                self._steps_ -= 1

            else:
                self._player_.move(self._player_._pos_)

    def draw(self):
        self._tilemap_.draw()
        self._player_.draw()

    def render_dbg(self):
        self._player_.render_position()

    def is_free(self) -> bool:
        self._player_._pos_ not in self._walls_


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

    def update(self):
        pass

    def draw(self):
        pyxel.bltm((self._x_ / 2) - (self._w_ / 2), (self._y_ / 2) - (self._h_ / 2), self._tm_, self._u_, self._v_, self._w_, self._h_)
