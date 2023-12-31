import sys

import pyxel

sys.path.append("../")

import maze
import conf 
from avatar import Position
from position_vec import pos_vec
from enemy import Wizard
from obstruct import Barrel
import player
from hellgirl import Portal

def construct(conf: conf.Conf) -> maze.Maze:
    # tile map number
    TM = 0

    TMAP1 = maze.TileMap(conf._x_, conf._y_, TM, 0, 0, 56, 48, 0)
    HALF_X = TMAP1._x_ / 2
    HALF_Y = TMAP1._y_ / 2
    HALF_H = TMAP1._h_ / 2
    HALF_YH = HALF_Y - HALF_H
    STEPS = 23
    PLAYER1 = player.Player((TMAP1._x_ / 2) + 12, (TMAP1._y_ / 2) - (TMAP1._h_ / 2), 0, 8, 0, 8, 8, 0)
    ENEMIES = [
        Wizard(84, 52), Wizard(76, 44), Wizard(68, 52),
        Barrel(60, 68), Barrel(60, 76), Barrel(76, 76), Barrel(84, 68)
    ]
    HELLGIRL = Portal(100, 76)

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

    return maze.Maze(TMAP1, STEPS, PLAYER1, ENEMIES, HELLGIRL, walls)
