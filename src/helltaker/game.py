import pyxel
import player

class App:
    def __init__(self):
        pyxel.init(160, 120, title="SFC Saver")
        pyxel.load("../../assets/resources/sample.pyxres")
        self._time_limit_ = 0
        self._energy_ = 3
        self._player_ = player.Player()

        pyxel.run(self.update, self.draw)

    def update(self):
        self._player_.update()
        if pyxel.btnp(pyxel.KEY_Q):
            pyxel.quit()

    def draw(self):
        self._player_.draw()
