from enum import Enum

import pyxel

import pane


class Congrats(pane.Pane):
    def __init__(self):
        super().__init__("Game Clear!!!")

    def update(self):
        pass

    def visible(self):
        self._is_visible_ = True
