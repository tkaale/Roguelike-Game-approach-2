import random


def put_player_on_board(board, place):
    board[place[0]][place[1]] = '๐บ'
    return board

# ๐ ๐ ๐ ๐ ๐ถ ๐ญ  ๐ฆ ๐ช ๐ช ๐น ๐ฆนโโ๏ธ ๐งก

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
        if board[coord_a][coord_b] == 'โฌ' or board[coord_a][coord_b] == '๐ฉ' or board[coord_a][coord_b] == '๐ฆ':
            break
        else:
            continue
    return [coord_a, coord_b]


    