import random

from level_one import MOUSE_ONE

def put_player_on_board(board, place):
    board[place[0]][place[1]] = '😺'
    return board



# 👑 💎 🔑 💊 🐶 🐭  🦈 🔪 🪓 🏹 🦹‍♀️ 🧡

def inventory_list(inventory):
    inventory_list = []
    for key in inventory:
        for i in range(0, inventory[key]):
            inventory_list.append(key)
    return inventory_list


def move_mouses_vertical(go_back):
    global MOUSE_ONE
    coord_a = MOUSE_ONE[0]
    coord_b = MOUSE_ONE[1]
    coord_a += 1
    if coord_a == go_back:
        while coord_a == MOUSE_ONE[0]:
            coord_a -= 1
    return [coord_a, coord_b]

print(move_mouses_vertical(MOUSE_ONE, 10))

def move_mouse_horizonal(coord, go_back):
    coord_a = coord[0]
    coord_b = coord[1]
    coord_b += 1
    if coord_b == go_back:
        while coord_b == coord[1]:
            coord_b -= 1
    return [coord_a, coord_b]


# def add_mouses(board,coord_a_start, coord_a_end, coord_b_start, coord_b_end):
#     while True:
#         coord_a = random.randint(coord_a_start, coord_a_end)
#         coord_b = random.randint(coord_b_start, coord_b_end)
#         if board[coord_a][coord_b] == '⬛' or board[coord_a][coord_b] == '🟩' or board[coord_a][coord_b] == '🟦':
#             break
#         else:
#             continue
#     return [coord_a, coord_b]
    