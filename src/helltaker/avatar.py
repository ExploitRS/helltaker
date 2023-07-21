import pyxel

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
