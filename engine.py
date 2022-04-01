import random

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


def add_mouses(board,coord_a_start, coord_a_end, coord_b_start, coord_b_end):
    while True:
        coord_a = random.randint(coord_a_start, coord_a_end)
        coord_b = random.randint(coord_b_start, coord_b_end)
        if board[coord_a][coord_b] == '⬛' or board[coord_a][coord_b] == '🟩' or board[coord_a][coord_b] == '🟦':
            break
        else:
            continue
    return [coord_a, coord_b]
    