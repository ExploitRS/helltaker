import sys

import pyxel

sys.path.append("../")

import maze
import conf 
from avatar import Position
from position_vec import pos_vec
import enemy
import player

def construct(conf: conf.Conf) -> maze.Maze:
    # tile map number
    TM = 0

    TMAP1 = maze.TileMap(conf._x_, conf._y_, TM, 0, 0, 56, 48, 0)
    STEPS = 16
    PLAYER1 = player.Player((TMAP1._x_ / 2) + 12, (TMAP1._y_ / 2) - (TMAP1._h_ / 2), 0, 8, 0, 8, 8, 0)
    ENEMIES1 = [enemy.Enemy()]

    walls = pos_vec()
    walls.append(
        Position(
            TMAP1._x_ / 2 + 20,
            ((TMAP1._y_ / 2) - (TMAP1._h_ / 2) - 8)
        ),
        Position(
            TMAP1._x_ / 2 - 8,
            ((TMAP1._y_ / 2) - (TMAP1._h_ / 2) - 8)
        ),
    )
    walls.append(
        Position(
            TMAP1._x_ / 2 - 12,
            TMAP1._y_ / 2 - TMAP1._h_ / 2,
        ), 
        Position(
            TMAP1._x_ / 2 - 20,
            TMAP1._y_ / 2 - TMAP1._h_ / 2,
        )
    )
    walls.append(
        Position(
            TMAP1._x_ / 2 - 28,
            TMAP1._y_ / 2 - (TMAP1._h_ / 2) + 8,
        ), 
        Position(
            TMAP1._x_ / 2 - 28,
            TMAP1._y_ / 2 - (TMAP1._h_ / 2) + 16,
        )
    )
    walls.append(
        Position(
            TMAP1._x_ / 2 - 36,
            TMAP1._y_ / 2 - (TMAP1._h_ / 2) + 24,
        ), 
        Position(
            TMAP1._x_ / 2 - 36,
            TMAP1._y_ / 2 - (TMAP1._h_ / 2) + 40,
        )
    )
    walls.append(
        Position(
            TMAP1._x_ / 2 + 20,
            TMAP1._y_ / 2 - (TMAP1._h_ / 2) + 48,
        ), 
        Position(
            TMAP1._x_ / 2 - 36,
            TMAP1._y_ / 2 - (TMAP1._h_ / 2) + 48,
        )
    )
    walls.append(
        Position(
            TMAP1._x_ / 2 + 20,
            TMAP1._y_ / 2 - (TMAP1._h_ / 2),
        ), 
        Position(
            TMAP1._x_ / 2 + 20,
            TMAP1._y_ / 2 - (TMAP1._h_ / 2) + 8,
        )
    )
    walls.append(
        Position(
            TMAP1._x_ / 2 + 12,
            TMAP1._y_ / 2 - (TMAP1._h_ / 2) + 16,
        ), 
        Position(
            TMAP1._x_ / 2 + 12,
            TMAP1._y_ / 2 - (TMAP1._h_ / 2) + 16,
        )
    )
    walls.append(
        Position(
            TMAP1._x_ / 2 + 12,
            TMAP1._y_ / 2 - (TMAP1._h_ / 2) + 24,
        ), 
        Position(
            TMAP1._x_ / 2 + 20,
            TMAP1._y_ / 2 - (TMAP1._h_ / 2) + 24,
        )
    )
    walls.append(
        Position(
            TMAP1._x_ / 2 + 28,
            TMAP1._y_ / 2 - (TMAP1._h_ / 2) + 32,
        ), 
        Position(
            TMAP1._x_ / 2 + 28,
            TMAP1._y_ / 2 - (TMAP1._h_ / 2) + 40,
        )
    )
    walls.append(
        Position(
            TMAP1._x_ / 2 + 20,
            TMAP1._y_ / 2 - (TMAP1._h_ / 2) + 32,
        ), 
        Position(
            TMAP1._x_ / 2 + 20,
            TMAP1._y_ / 2 - (TMAP1._h_ / 2) + 32,
        )
    )
    walls.append(
        Position(
            TMAP1._x_ / 2 + 4,
            TMAP1._y_ / 2 - (TMAP1._h_ / 2) + 24,
        ), 
        Position(
            TMAP1._x_ / 2 - 12,
            TMAP1._y_ / 2 - (TMAP1._h_ / 2) + 24,
        )
    )

    walls = walls.build()

    return maze.Maze(TMAP1, STEPS, PLAYER1, ENEMIES1, [48, 40], walls)
