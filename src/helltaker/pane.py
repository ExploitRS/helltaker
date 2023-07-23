from enum import Enum

import pyxel

class Method():
    def __init__(self, label, fn):
        self._label_ = label
        self._fn_ = fn

    def update(self):
        self._fn_()

class ComponentKind(Enum):
    Text = 1
    Method = 2

class Component():
    def __init__(self, kind: ComponentKind, val):
        self._kind_ = kind
        match kind:
            case ComponentKind.Text:
                self._text_ = val

            case ComponentKind.Method:
                self._method_ = val

            case _:
                return

class Pane:
    def __init__(self, title: str, show = None, next_pane = None):
        self._title_ = title
        self._components_ = []
        self._next_pane_ = next_pane
        self._display_fn_ = show
        self._is_visible_ = False
        self._action_ = ""

    def update(self):
        if self._is_visible_:
            method_components = list(filter(lambda x: x._kind_ == ComponentKind.Method, self._components_))
            # key_events = [x._methods_._key_event_ for x in method_components]
            for m in method_components:
                m._method_.update()

        # if self._next_pane_ != None:
        #     if pyxel.btn(pyxel.KEY_ESC):
        #         self._next_pane_()

    def render(self):
        if self._is_visible_:
            pyxel.text(35, 46, self._title_, 13)
            for c in self._components_:
                match c._kind_:
                    case ComponentKind.Text:
                        pyxel.text(35, 66, c._text_, pyxel.frame_count % 16)
                    case ComponentKind.Method:
                        pyxel.text(35, 86, c._method_._label_, 13)
                    case _: pass

