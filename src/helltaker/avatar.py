import pyxel

import player

class Position:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def sub_update(self, other_x, other_y):
        self.x = self.x + other_x
        self.y = self.y + other_y

    def __eq__(self, other) -> bool:
        if (self.x == other.x) and (self.y == other.y):
            return True

class Avatar:
    def __init__(self, x, y, img, u, v, w, h, col):
        self._pos_ = Position(x, y)
        self._img_ = img
        self._u_   = u
        self._v_   = v
        self._w_   = w
        self._h_   = h
        self._col_ = col

    def update(self):
        pass

    def draw(self):
        pyxel.blt(
            self._pos_.x,
            self._pos_.y,
            self._img_,
            self._u_,
            self._v_,
            self._w_,
            self._h_,
            self._col_,
        )

    def pos(self) -> Position:
        return self._pos_

if __name__ == "__main__":
    pos = Position(0, 0)
    ex1 = Position(0, 0)
    ex2 = Position(1, 1)
    ex3 = Position(1.0, 1.0)
    lst = [ex1, ex2]

    if pos == ex1:
        print("pos and ex1 is same")

    if pos == ex2:
        print("pos and ex2 is same")

    if ex2 == ex3:
        print("ex2 and ex3 is same")
    if pos in lst:
        print("lst contain pos")

    pos2 = pos
    pos3 = Position(0, 0)
    pos3 = pos
    pos2.x = 1

    print(f"pos1: {pos.x}")
    print(f"pos2: {pos2.x}")
    print(f"pos3: {pos3.x}")

    print(f"pos: {type(pos)}")
    print(f"ex1: {type(ex1)}")
    print(f"ex2: {type(ex2)}")
