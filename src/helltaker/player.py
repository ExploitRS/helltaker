from enum import Enum
import pyxel

class Player:
    def __init__(self):
        self._x_ = 72
        self._y_ = 32
        self._direction_ = None

    def update(self):
        if pyxel.btn(pyxel.KEY_LEFT) or pyxel.btn(pyxel.GAMEPAD1_BUTTON_DPAD_LEFT) or pyxel.btn(pyxel.KEY_A):
            self._x_ = max(self._x_ - 2, 0)

        if pyxel.btn(pyxel.KEY_RIGHT) or pyxel.btn(pyxel.GAMEPAD1_BUTTON_DPAD_RIGHT) or pyxel.btn(pyxel.KEY_D):
            self._x_ = min(self._x_ + 2, pyxel.width -16)

        if pyxel.btn(pyxel.KEY_UP) or pyxel.btn(pyxel.GAMEPAD1_BUTTON_DPAD_UP) or pyxel.btn(pyxel.KEY_W):
            self._y_ = self._y_ - 2

        if pyxel.btn(pyxel.KEY_DOWN) or pyxel.btn(pyxel.GAMEPAD1_BUTTON_DPAD_DOWN) or pyxel.btn(pyxel.KEY_S):
            self._y_ = self._y_ + 2

    def draw(self):
        pyxel.blt(
            self._x_,
            self._y_,
            0,
            8,
            0,
            8,
            8,
            0,
        )

class Direction(Enum):
    Right = 1
    Left  = 2
    Up    = 3
    Down  = 4