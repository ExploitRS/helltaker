import pyxel

from avatar import Avatar, Position, Direction

class Portal(Avatar):
    def __init__(self, x, y):
        super().__init__(x, y, 0, 16, 32, 8, 8, 0)

    def neighbor_vec(self) -> list[Position]:
        p = self._pos_
        return [
            p + Direction.Left.value, p + Direction.Right.value,
            p + Direction.Up.value, p + Direction.Down.value
        ]
