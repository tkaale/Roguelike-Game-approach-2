import random

def put_player_on_board(board, place):
    board[place[0]][place[1]] = '😺'
    return board

#inventory

# 👑 💎 🔑 💊 🐶 🐭  🦈 🔪 🪓 🏹 🦹‍♀️ 

INVENTORY= {'🪓': 1, '🔪': 1, '💎': 5, '🔑': 1, }

def inventory_list(inventory):
    inventory_list = []
    for key in inventory:
        for i in range(0, inventory[key]):
            inventory_list.append(key)
    return inventory_list


def get_random_coordinates(inventory):
    random_coordinates = []
    for key in inventory.keys(): 
        for counter in range(0, inventory[key]):
            first_coord = random.randint(1,20)
            second_coord = random.randint(1,28)
            random_coordinates.append([first_coord, second_coord])
    return random_coordinates

print(get_random_coordinates(INVENTORY))