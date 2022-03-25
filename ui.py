def display_window(window):
    for sublist in window:
        print(''.join(sublist))

def add_gate_to_board(board, gate):
     board[gate[0]][gate[1]] = '🪜'
     return board