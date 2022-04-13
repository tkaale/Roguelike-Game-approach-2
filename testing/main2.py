import util2
import ui2

COORD_A = 1
COORD_B = 1
INVENTORY= {'🪓': 0, '🔪': 0, '💎': 0, '🔑': 0}
LIVES = {'🧡': '🟥🟥🟥🟥🟥'}

BOARD = ui2.board('1')

def move(board):
    global coord_a, coord_b
    while True:
        key = util2.key_pressed()
        if key.upper() == 'W':
            coord_a -= 1
            if [coord_a, coord_b] in ui2.check_walls(board):
                        coord_a += 1
        if key.upper() == 'S':
            coord_a += 1
            if [coord_a, coord_b] in ui2.check_walls(board):
                        coord_a -= 1
        if key.upper() == 'D':
            coord_b += 1
            if [coord_a, coord_b] in ui2.check_walls(board):
                        coord_b -= 1
        if key.upper() == 'A':
            coord_b -= 1
            if [coord_a, coord_b] in ui2.check_walls(board):
                        coord_b += 1
        return([coord_a, coord_b])

ui2.display_board(BOARD)