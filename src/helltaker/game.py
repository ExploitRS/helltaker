from copy import deepcopy
import argparse

import pyxel

import nav
import maze
import conf
from avatar import Avatar, Position
import player
import enemy
from maze_i import maze_i
from position_vec import colorise
from congrats_pane import Congrats

class App:
    def __init__(self, is_debug: bool):
        GAME_HEIGHT = 120
        GAME_WIDTH = 160
        GAME_TITLE = "SFC Saver"

        config = conf.Conf(GAME_WIDTH, GAME_HEIGHT, GAME_TITLE)

        pyxel.init(GAME_WIDTH, GAME_HEIGHT, title=GAME_TITLE)
        pyxel.load("../../assets/resources/hell.pyxres")
        pyxel.tilemap(0)


        MAZE_I = maze_i.construct(config)
        mazes = [ MAZE_I ]
        self._maze_list_ = mazes
        self._maze_vec_default_ = deepcopy(mazes)

        self._time_limit_ = 0
        self._energy_ = 3
        self._stage_num_ = 1
        self._is_debug_ = is_debug
        self._congraz_pane_ = Congrats()

        self._time_obj_ = nav.Pallet(10, 10, self._time_limit_, 7)
        self._life_count_obj_ = nav.Pallet(10, (GAME_HEIGHT - 10), self._maze_list_[0]._steps_, 7)
        self._stage_num_obj_ = nav.Pallet((GAME_WIDTH - 10), (GAME_HEIGHT - 10), self._stage_num_, 7)

        self._nav_ = nav.Nav(self._time_obj_, self._life_count_obj_, self._stage_num_obj_)

        pyxel.run(self.update, self.draw)

    def update(self):
        if len(self._maze_list_) <= 0:
            self._congraz_pane_.visible()
            self._congraz_pane_.update()

            if self._congraz_pane_._action_ == "restart":
                self._maze_list_ = deepcopy(self._maze_vec_default_)
                self._congraz_pane_.invisible()
                self._congraz_pane_._action_ = ""

        elif self._maze_list_[0]._is_clear_:
            self._maze_list_.pop(0)

        else:
            self._maze_list_[0].update()
            self._time_obj_._text_ = str(self._time_limit_)
            self._life_count_obj_._text_ = str(self._maze_list_[0]._steps_)
            self._stage_num_obj_._text_ = str(self._stage_num_)

        if pyxel.btnp(pyxel.KEY_Q):
            pyxel.quit()

    def draw(self):
        pyxel.cls(0)

        if len(self._maze_list_) > 0:
            self._maze_list_[0].draw()
            self._nav_.draw()

            if self._is_debug_:
                self._maze_list_[0].render_dbg()
                colorise(self._maze_list_[0]._walls_, 8)

        else:
            self._congraz_pane_.render()
