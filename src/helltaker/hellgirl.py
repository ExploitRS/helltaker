import pyxel

from avatar import Avatar

class Portal(Avatar):
    def __init__(self, x, y):
        super().__init__(x, y, 0, 16, 32, 8, 8, 0)
