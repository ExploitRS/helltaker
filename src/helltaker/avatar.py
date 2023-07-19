import pyxel

class Avatar:
    def __init__(self, x, y, img, u, v, w, h, col):
        self._x_   = x
        self._y_   = y
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
            self._x_,
            self._y_,
            self._img_,
            self._u_,
            self._v_,
            self._w_,
            self._h_,
            self._col_,
        )