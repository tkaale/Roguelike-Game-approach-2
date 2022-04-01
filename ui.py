def display_window(window):
    for sublist in window:
        print(''.join(sublist))

def display_inventory(inventory):
    inventory_list = []
    for key in inventory:
        inventory_list.append(f"{key}: {inventory[key]}")
    print('   '.join(inventory_list))


def add_gate_to_board(board, gate):
     board[gate[0]][gate[1]] = '🪜'
     return board

def check_walls(board):
    walls_coordinates = [[21, 0], [21, 1], [21, 2], [21, 3], [21, 4], [21, 5], [21, 6], [21, 7], [21, 8], [21, 9], [21, 10], [21, 11], [21, 12], [21, 13], [21, 14], [21, 15], [21, 16], [21, 17], [21, 18], [21, 19], [21, 20], [21, 21], [21, 22], [21, 23], [21, 24], [21, 25], [21, 26], [21, 27], [21, 28], [21, 29]]
    for sublist in board:
        for i in range(-1, len(sublist)):
            check = sublist[i]
            if check == '🧱':
                walls_coordinates.append([board.index(sublist), i])
            if check == '🌳':
                walls_coordinates.append([board.index(sublist), i])
            if check == '🌊':
                walls_coordinates.append([board.index(sublist), i])
    return walls_coordinates