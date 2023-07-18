# def hello():
#     return "Hello from helltaker!"

import pyxel
import random

# マップのサイズ
MAP_WIDTH = 20
MAP_HEIGHT = 15

# タイルのサイズ
TILE_SIZE = 8

# プレイヤーの初期位置
player_x = MAP_WIDTH // 2
player_y = MAP_HEIGHT // 2

# 洞窟のマップデータ
cave_map = []

# マップの初期化
def init_map():
    for y in range(MAP_HEIGHT):
        row = []
        for x in range(MAP_WIDTH):
            if random.random() < 0.4:  # 40%の確率で壁を生成
                row.append(1)  # 壁
            else:
                row.append(0)  # 床
        cave_map.append(row)

# ゲームの更新処理
def update():
    global player_x, player_y

    # プレイヤーの移動
    if pyxel.btnp(pyxel.KEY_LEFT):
        if player_x > 0 and cave_map[player_y][player_x - 1] == 0:
            player_x -= 1

    elif pyxel.btnp(pyxel.KEY_RIGHT):
        if player_x < MAP_WIDTH - 1 and cave_map[player_y][player_x + 1] == 0:
            player_x += 1

    elif pyxel.btnp(pyxel.KEY_UP):
        if player_y > 0 and cave_map[player_y - 1][player_x] == 0:
            player_y -= 1

    elif pyxel.btnp(pyxel.KEY_DOWN):
        if player_y < MAP_HEIGHT - 1 and cave_map[player_y + 1][player_x] == 0:
            player_y += 1

# ゲームの描画処理
def draw():
    pyxel.cls(0)  # 背景色を黒に設定

    # マップの描画
    for y in range(MAP_HEIGHT):
        for x in range(MAP_WIDTH):
            if cave_map[y][x] == 1:
                pyxel.rect(x * TILE_SIZE, y * TILE_SIZE, TILE_SIZE, TILE_SIZE, 7)  # 壁を描画
            else:
                pyxel.rect(x * TILE_SIZE, y * TILE_SIZE, TILE_SIZE, TILE_SIZE, 3)  # 床を描画

    # プレイヤーの描画
    pyxel.rect(player_x * TILE_SIZE, player_y * TILE_SIZE, TILE_SIZE, TILE_SIZE, 9)

# ゲームの実行
def run():
    pyxel.init(MAP_WIDTH * TILE_SIZE, MAP_HEIGHT * TILE_SIZE)
    init_map()
    pyxel.run(update, draw)

run()