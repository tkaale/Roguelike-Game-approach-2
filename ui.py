def display_window(window):
    for sublist in window:
        print(''.join(sublist))

def add_gate_to_board(board, gate):
     board[gate[0]][gate[1]] = '🪜'
     return board

def check_walls(board):
    walls_coordinates = []
    for sublist in board:
        for i in range(0, len(sublist)):
            check = sublist[i]
            if check == '🧱':
                walls_coordinates.append([board.index(sublist), i])
    return walls_coordinates