import util2
import ui2
import engine2

COORD_A = 1
COORD_B = 1
INVENTORY= {'🪓': 0, '🔪': 0, '💎': 0, '🔑': 0}
LIVES = {'🧡': '🟥🟥🟥🟥🟥'}

BOARD_ONE = ui2.board('1')
BOARD_TWO = ui2.board('2')
BOARD_THREE = ui2.board('3')

def move(board):
    global COORD_A, COORD_B
    while True:
        key = util2.key_pressed()
        if key.upper() == 'W':
            COORD_A -= 1
            if [COORD_A, COORD_B] in ui2.check_walls(board):
                        COORD_A += 1
        if key.upper() == 'S':
            COORD_A += 1
            if [COORD_A, COORD_B] in ui2.check_walls(board):
                        COORD_A -= 1
        if key.upper() == 'D':
            COORD_B += 1
            if [COORD_A, COORD_B] in ui2.check_walls(board):
                        COORD_B -= 1
        if key.upper() == 'A':
            COORD_B -= 1
            if [COORD_A, COORD_B] in ui2.check_walls(board):
                        COORD_B += 1
        return([COORD_A, COORD_B])

def main():
    global COORD_A, COORD_B, BOARD_ONE
    board = BOARD_ONE
    engine2.put_player_on_board(board, [COORD_A, COORD_B])
    ui2.display_board(board)
    while True:
        coord = move(board)
        util2.clear_screen()
        board = ui2.board('1')
        engine2.put_player_on_board(board, coord)
        ui2.display_board(board)


if __name__ == '__main__':
    main()