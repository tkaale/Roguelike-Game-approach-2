import ui
import level_one, level_two, level_three
import util
import engine 


coord_a = 1
coord_b = 1
INVENTORY= {'🪓': 0, '🔪': 0, '💎': 0, '🔑': 0}
LIVES = {'🧡': 100}


def move(board):
    global coord_a, coord_b
    while True:
        key = util.key_pressed()
        if key.upper() == 'W':
            coord_a -= 1
            if [coord_a, coord_b] in ui.check_walls(board):
                        coord_a += 1
        if key.upper() == 'S':
            coord_a += 1
            if [coord_a, coord_b] in ui.check_walls(board):
                        coord_a -= 1
        if key.upper() == 'D':
            coord_b += 1
            if [coord_a, coord_b] in ui.check_walls(board):
                        coord_b -= 1
        if key.upper() == 'A':
            coord_b -= 1
            if [coord_a, coord_b] in ui.check_walls(board):
                        coord_b += 1
        return([coord_a, coord_b])




def main():
    global coord_a, coord_b
    board = level_one.board_level_one()
    engine.put_player_on_board(board, [coord_a, coord_b])
    ui.display_window(board)
    ui.display_inventory(INVENTORY)
    ui.display_inventory(LIVES)

    while True:
        coord = move(board)
        util.clear_screen()
        board = level_one.board_level_one()
        engine.put_player_on_board(board, coord)
        ui.display_window(board)
        ui.display_inventory(INVENTORY)
        ui.display_inventory(LIVES)


#level TWO
        if coord == level_one.GATE_ONE:
            coord_a = 1
            coord_b = 1
            util.clear_screen()
            board = level_two.board_level_two()
            engine.put_player_on_board(board, [coord_a, coord_b])
            ui.display_window(board)
            while True:
                coord = move(board)
                util.clear_screen()
                board = level_two.board_level_two()
                engine.put_player_on_board(board, coord)
                ui.display_window(board)
#level THREE
                if coord == level_two.GATE_TWO:
                    coord_a = 1
                    coord_b = 1
                    util.clear_screen()
                    board = level_three.board_level_three()
                    engine.put_player_on_board(board, [coord_a, coord_b])
                    ui.display_window(board)
                    while True:
                        coord = move(board)
                        util.clear_screen()
                        board = level_three.board_level_three()
                        engine.put_player_on_board(board, coord)
                        ui.display_window(board)


if __name__ == '__main__':
    main()


# def main():
#     util.clear_screen()
#     global coord_a, coord_b
#     while True:
#         board = level_one.board_level_one()
#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 sys.exit()
#             if event.type == pygame.KEYDOWN:
#                 if event.key == pygame.K_w:
#                     coord_a -= 1
#                     if [coord_a, coord_b] in ui.check_walls(board):
#                         coord_a += 1
#                 if event.key == pygame.K_s:
#                     coord_a += 1
#                     if [coord_a, coord_b] in ui.check_walls(board):
#                         coord_a -= 1
#                 if event.key == pygame.K_d:
#                     coord_b += 1
#                     if [coord_a, coord_b] in ui.check_walls(board):
#                         coord_b -= 1
#                 if event.key == pygame.K_a:
#                     coord_b -= 1
#                     if [coord_a, coord_b] in ui.check_walls(board):
#                         coord_b += 1
#                 util.clear_screen()
#                 board = level_one.board_level_one()
#                 engine.put_player_on_board(board, [coord_a, coord_b])
#                 ui.display_window(board) 











# def main():
#     global coord_a, coord_b
#     while True:
#         if event.key == pygame.K_w:
#             coord_a -= 1
#         if event.key == pygame.K_s:
#             coord_a += 1
#         if event.key == pygame.K_d:
#             coord_b += 1
#         if event.key == pygame.K_a:
#             coord_b -= 1
#         window_game = window()
#         generate_board(5,5, window_game, [30,4], [32,9])
#         window_game = put_player_on(window_game, [coord_a, coord_b])
#         ui.display_window(window_game)








# def generate_board(height, width, window_lst, start_coordinate, gate): 
#     coordinate_down = [start_coordinate[0] + height, start_coordinate[1]]
#     coordinate_right = [start_coordinate[0], start_coordinate[1] + width]
#     for i in range(0, width):
#         window_lst[start_coordinate[0]][start_coordinate[1] + i] = '■'
#         window_lst[coordinate_down[0]][coordinate_down[1] + i] = '■'
#     for i in range(0, height):
#         window_lst[start_coordinate[0] + i][start_coordinate[1]] = '■'
#     for i in range(0, height + 1):
#         window_lst[coordinate_right[0] + i][coordinate_right[1]] = '■'
#     window_lst[gate[0]][gate[1]] = '□'
#     return window_lst


# def put_player_on(board, place):
#     board[place[0]][place[1]] = '₿'
#     return board



# def generate_board(height, width):   # □
#     board_lst_of_lst = []
#     for i in range(0,height):
#         board_lst_of_lst.append(['.'] * width)
#     board_lst_of_lst.insert(0, ['■'] * width)
#     board_lst_of_lst.insert(len(board_lst_of_lst), ['■'] * width)  #█
#     for i in range(1, len(board_lst_of_lst)-1):
#         board_lst_of_lst[i][0] = '■'
#         board_lst_of_lst[i][-1] = '■'
#     return board_lst_of_lst


# def add_gate_to_board(board, gate):
#      board[gate[0]][gate[1]] = '□'
#      return board

# def put_player_on_board(board, place):
#     board[place[0]][place[1]] = '₿'
#     return board




# def main():
#     global coord_a, coord_b
#     while True:
#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 sys.exit()
#             if event.type == pygame.KEYDOWN:
#                 if event.key == pygame.K_w:
#                     coord_a -= 1
#                 if event.key == pygame.K_s:
#                     coord_a += 1
#                 if event.key == pygame.K_d:
#                     coord_b += 1
#                 if event.key == pygame.K_a:
#                     coord_b -= 1
#                 gate = [3,14]
#                 board = generate_board(10,15)
#                 board = add_gate_to_board(board, gate)
#                 if coord_a == 0:
#                     coord_a = 1
#                 if coord_b == 0:
#                     coord_b = 1
#                 if coord_a == 11:
#                     coord_a = 10
#                 if coord_b == 14:
#                     if coord_a == 3:
#                         coord_b = 14
#                     else:
#                         coord_b = 13
#                 board = put_player_on_board(board, [coord_a, coord_b])
#                 time.sleep(0)
#                 for i in range(100):
#                     print('')
#                 ui.display_board(board)
#                 print([coord_a, coord_b])