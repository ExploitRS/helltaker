import pyxel
import numpy as np

from avatar import Position

class pos_vec:

    def __init__(self):
        self._ls_: list[tuple] = []

    def append(self, base: Position, dest: Position):
        self._ls_.append((base, dest))

    def build(self) -> list[Position]:
        ret: list[Position] = []

        for e in self._ls_:
            base, dest = e

            dx = 8.0 if dest.x >= base.x else -8.0
            dy = 8.0 if dest.y >= base.y else -8.0

            for y in np.arange(base.y, dest.y + dy, dy):
                for x in np.arange(base.x, dest.x + dx, dx):
                    ret.append(Position(x, y))

        return ret
