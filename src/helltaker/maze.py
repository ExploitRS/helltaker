from enum import Enum
from copy import deepcopy

import pyxel

import conf
from player import Player
from enemy import Enemy
from avatar import Position, Direction

class Maze:
    def __init__(self, tm, steps, player: Player, enemies: list[Enemy], end_pos, walls):
        self._tilemap_        = tm
        self._is_clear_       = False
        self._steps_          = steps
        self._max_steps_      = steps
        self._player_         = player 
        self._enemies_        = enemies
        self._enemies_default_ = enemies.copy()
        self._end_pos_        = end_pos
        self._walls_          = walls
 
    def update(self):
        if 0 >= self._steps_:
            self._player_.reset_pos()
            self._steps_ = self._max_steps_
            self._enemies_ = self._enemies_default_.copy()
            _ = list(map(lambda x: x.respawn(), self._enemies_))

        if pyxel.btnp(pyxel.KEY_LEFT) or pyxel.btnp(pyxel.GAMEPAD1_BUTTON_DPAD_LEFT) or pyxel.btnp(pyxel.KEY_A):
            dir = Direction.Left
            dec_step = 1
            neighbor = self._player_.neighbor(dir)
            enemies_pos = [x._pos_ for x in self._enemies_]

            if neighbor in self._walls_:
                self._player_.move(self._player_._pos_)
                return

            elif neighbor in enemies_pos:
                enemy = list(filter(lambda x: x._pos_ == neighbor, self._enemies_))

                if enemy[0].neighbor(dir) in self._walls_:
                    enemy[0]._is_alive_ = False
                    self._enemies_.remove(enemy[0])

                elif enemy[0].neighbor(dir) in enemies_pos:
                    return

                else:
                    enemy[0].move(neighbor + dir.value)

                self._steps_ -= enemy[0]._damage_
                return

            self._player_.move(neighbor)
            self._steps_ -= dec_step

        if pyxel.btnp(pyxel.KEY_RIGHT) or pyxel.btnp(pyxel.GAMEPAD1_BUTTON_DPAD_RIGHT) or pyxel.btnp(pyxel.KEY_D):
            dir = Direction.Right
            dec_step = 1
            neighbor = self._player_.neighbor(dir)
            enemies_pos = [x._pos_ for x in self._enemies_]

            if neighbor in self._walls_:
                self._player_.move(self._player_._pos_)
                return

            elif neighbor in enemies_pos:
                enemy = list(filter(lambda x: x._pos_ == neighbor, self._enemies_))

                if enemy[0].neighbor(dir) in self._walls_:
                    enemy[0]._is_alive_ = False
                    self._enemies_.remove(enemy[0])

                elif enemy[0].neighbor(dir) in enemies_pos:
                    return

                else:
                    enemy[0].move(neighbor + dir.value)

                self._steps_ -= enemy[0]._damage_
                return

            self._player_.move(neighbor)
            self._steps_ -= dec_step

        if pyxel.btnp(pyxel.KEY_UP) or pyxel.btnp(pyxel.GAMEPAD1_BUTTON_DPAD_UP) or pyxel.btnp(pyxel.KEY_W):
            dir = Direction.Up
            dec_step = 1
            neighbor = self._player_.neighbor(dir)
            enemies_pos = [x._pos_ for x in self._enemies_]

            if neighbor in self._walls_:
                self._player_.move(self._player_._pos_)
                return

            elif neighbor in enemies_pos:
                enemy = list(filter(lambda x: x._pos_ == neighbor, self._enemies_))

                if enemy[0].neighbor(dir) in self._walls_:
                    enemy[0]._is_alive_ = False
                    self._enemies_.remove(enemy[0])

                elif enemy[0].neighbor(dir) in enemies_pos:
                    return

                else:
                    enemy[0].move(neighbor + dir.value)

                self._steps_ -= enemy[0]._damage_
                return

            self._player_.move(neighbor)
            self._steps_ -= dec_step

        if pyxel.btnp(pyxel.KEY_DOWN) or pyxel.btnp(pyxel.GAMEPAD1_BUTTON_DPAD_DOWN) or pyxel.btnp(pyxel.KEY_S):
            dir = Direction.Down
            dec_step = 1
            neighbor = self._player_.neighbor(dir)
            enemies_pos = [x._pos_ for x in self._enemies_]

            if neighbor in self._walls_:
                self._player_.move(self._player_._pos_)
                return

            elif neighbor in enemies_pos:
                enemy = list(filter(lambda x: x._pos_ == neighbor, self._enemies_))

                if enemy[0].neighbor(dir) in self._walls_:
                    enemy[0]._is_alive_ = False
                    self._enemies_.remove(enemy[0])

                elif enemy[0].neighbor(dir) in enemies_pos:
                    return

                else:
                    enemy[0].move(neighbor + dir.value)

                self._steps_ -= enemy[0]._damage_
                return

            self._player_.move(neighbor)
            self._steps_ -= dec_step

    def draw(self):
        self._tilemap_.draw()
        self._player_.draw()
        for e in self._enemies_:
            e.render()

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
