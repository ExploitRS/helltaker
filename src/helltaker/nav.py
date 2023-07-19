import pyxel

class Nav:
    def __init__(self, stage_num, life_count, time):
        self._stage_num_ = stage_num
        self._life_count_ = life_count
        self._time_ = time

    def update(self):
        pass

    def draw(self):
        self._stage_num_.draw()
        self._life_count_.draw()
        self._time_.draw()

class Pallet:
    def __init__(self, x, y, text, col):
        self._x_ = x
        self._y_ = y
        self._text_: str = text
        self._col_ = col

    def update(self):
        pass

    def draw(self):
        pyxel.text(self._x_, self._y_, self._text_, self._col_)