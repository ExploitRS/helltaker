import pyxel

from avatar import Avatar, Position

class Enemy(Avatar):
    def __init__(self, x, y, img, u, v, w, h, col, damage):
        super().__init__(x, y, img, u, v, w, h, col)
        self._damage_ = damage

class Wizard(Enemy):
    def __init__(self, x, y):
        DAMAGE = 1
        super().__init__(x, y, 0, 64, 8, 8, 8, 0, DAMAGE)
