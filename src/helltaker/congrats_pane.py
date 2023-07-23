from enum import Enum

import pyxel

from pane import Pane, Component, ComponentKind, Method

class Congrats(Pane):
    def __init__(self):
        super().__init__("Congraz!!!")
        print(self._action_)
        def restart_cap():
            if pyxel.btnp(pyxel.KEY_SPACE):
                self._action_ = "restart"

        self._components_.append(Component(ComponentKind.Text, "Game Clear!!!"))
        m = Method("- Restart [ SPACE ]-", restart_cap)
        self._components_.append(Component(ComponentKind.Method, m))

    def visible(self):
        self._is_visible_ = True

    def invisible(self):
        self._is_visible_ = False
