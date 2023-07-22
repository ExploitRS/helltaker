import pyxel

from avatar import Avatar, Position
from obstract import Obstract

class Enemy(Obstract):
    pass

class Wizard(Enemy):
    def __init__(self, x, y):
        DAMAGE = 1
        super().__init__(x, y, 0, 64, 8, 8, 8, 0, DAMAGE)
