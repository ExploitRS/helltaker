import pyxel

from avatar import Avatar

class Obstract(Avatar):
    def __init__(self, x, y, img, u, v, w, h, col, damage, is_alive = True):
        super().__init__(x, y, img, u, v, w, h, col)
        self._damage_ = damage
        self.default_alive = is_alive
        self._is_alive_ = is_alive

    def respawn(self):
        self.reset_pos()
        self._is_alive_ = self.default_alive

    def render(self):
        if self._is_alive_:
            self.draw()

class Barrel(Obstract):
    def __init__(self, x, y):
        DAMAGE = 1
        super().__init__(x, y, 0, 80, 24, 8, 8, 0, DAMAGE)
