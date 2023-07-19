from enum import Enum

import pyxel

from avatar import Avatar

class Player(Avatar):
    def update(self):
        if pyxel.btnp(pyxel.KEY_LEFT) or pyxel.btnp(pyxel.GAMEPAD1_BUTTON_DPAD_LEFT) or pyxel.btnp(pyxel.KEY_A):
            self._x_ = max(self._x_ - 8, 0)

        if pyxel.btnp(pyxel.KEY_RIGHT) or pyxel.btnp(pyxel.GAMEPAD1_BUTTON_DPAD_RIGHT) or pyxel.btnp(pyxel.KEY_D):
            self._x_ = min(self._x_ + 8, pyxel.width -16)

        if pyxel.btnp(pyxel.KEY_UP) or pyxel.btnp(pyxel.GAMEPAD1_BUTTON_DPAD_UP) or pyxel.btnp(pyxel.KEY_W):
            self._y_ = self._y_ - 8

        if pyxel.btnp(pyxel.KEY_DOWN) or pyxel.btnp(pyxel.GAMEPAD1_BUTTON_DPAD_DOWN) or pyxel.btnp(pyxel.KEY_S):
            self._y_ = self._y_ + 8

class Direction(Enum):
    Right = 1
    Left  = 2
    Up    = 3
    Down  = 4