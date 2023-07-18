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