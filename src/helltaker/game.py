import pyxel
import player
import nav
import maze
import conf

class App:
    def __init__(self):
        GAME_HEIGHT = 120
        GAME_WIDTH = 160
        GAME_TITLE = "SFC Saver"

        config = conf.Conf(GAME_WIDTH, GAME_HEIGHT, GAME_TITLE)

        pyxel.init(GAME_WIDTH, GAME_HEIGHT, title=GAME_TITLE)
        pyxel.load("../../assets/resources/hell.pyxres")

        MAZES = init_maze_list(config)
        self._maze_list_ = MAZES

        self._time_limit_ = 0
        self._energy_ = 3
        self._stage_num_ = 1
        self._player_ = player.Player()

        self._time_obj_ = nav.Pallet(10, 10, self._time_limit_, 7)
        self._life_count_obj_ = nav.Pallet(10, (GAME_HEIGHT - 10), self._energy_, 7)
        self._stage_num_obj_ = nav.Pallet((GAME_WIDTH - 10), (GAME_HEIGHT - 10), self._stage_num_, 7)

        self._nav_ = nav.Nav(self._time_obj_, self._life_count_obj_, self._stage_num_obj_)

        pyxel.run(self.update, self.draw)

    def update(self):
        self._player_.update()
        self._time_obj_._text_ = str(self._time_limit_)
        self._life_count_obj_._text_ = str(self._energy_)
        self._stage_num_obj_._text_ = str(self._stage_num_)

        if pyxel.btnp(pyxel.KEY_Q):
            pyxel.quit()

    def draw(self):
        self._maze_list_[0].draw()
        self._player_.draw()
        self._nav_.draw()

def init_maze_list(conf: conf.Conf) -> list[maze.Maze]:
    TM = 0
    MAZE1 = maze.Maze(conf, TM, 0, 0, 56, 48, 0)
    return [ MAZE1 ]
