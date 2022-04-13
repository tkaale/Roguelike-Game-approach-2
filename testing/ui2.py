

def board(level):
    if level == '1':
        board_list = []
        for i in range(0,20):
            board_list.append(['⬛'] * 30)  #⬜
        board_list.insert(0, ['🧱'] * 30)
        board_list.insert(len(board_list), ['🧱'] *   30)
        for i in range(1, len(board_list) -1):
            board_list[i][0] = '🧱'
            board_list[i][-1] = '🧱'
        for i in range(0,8):
            board_list[10][12 + i] = '🧱'
            board_list[13 + i][25] = '🧱'
            board_list[4][15 + i] = '🧱'
            board_list[8 + i][4] = '🧱'
            board_list[18][19 + i] = '🧱'
        for i in range(0,5):
            board_list[2][i] = '🧱'
            board_list[15][10 + i] = '🧱'
            board_list[i][23] = '🧱'
            board_list[2 + i][5] = '🧱'
            board_list[8 + i][15] = '🧱'
            board_list[17][2 + i] = '🧱'
            board_list[12][4 + i] = '🧱'
        for i in range(0,3):
            board_list[5][3 + i] = '🧱'
            board_list[10 + i][19] = '🧱'
            board_list[10 + i][19] = '🧱'
            board_list[19][2 + i] = '🧱'
            board_list[4 + i][10] = '🧱'
            board_list[10][26 + i] = '🧱'
            board_list[6 + i][24] = '🧱'
    if level == '2':
        board_list = []
        for i in range(0,20):
            board_list.append(['🟩'] * 30)  #⬜
        board_list.insert(0, ['🌳'] * 30)
        board_list.insert(len(board_list), ['🌳'] *   30)
        for i in range(1, len(board_list) -1):
            board_list[i][0] = '🌳'
            board_list[i][-1] = '🌳'
        for i in range(0,8):
            board_list[5][3 + i] = '🌳'
            board_list[10 + i][19] = '🌳'
            board_list[4][15 + i] = '🌳'
            board_list[10 + i][19] = '🌳'
            board_list[19][2 + i] = '🌳'
            board_list[4 + i][10] = '🌳'
            board_list[12][4 + i] = '🌳'  
        for i in range(0,5):
            board_list[10][12 + i] = '🌳'
            board_list[10][12 + i] = '🌳'
            board_list[13 + i][25] = '🌳'
            board_list[5][3 + i] = '🌳'
            board_list[10 + i][19] = '🌳'
            board_list[6 + i][24] = '🌳'
            board_list[8 + i][15] = '🌳'
            board_list[17][2 + i] = '🌳'      
        for i in range(0,3):
            board_list[2][i] = '🌳'
            board_list[15][10 + i] = '🌳'
            board_list[i][23] = '🌳'
            board_list[2 + i][5] = '🌳'
            board_list[8 + i][4] = '🌳'
            board_list[18][19 + i] = '🌳'
            board_list[10][26 + i] = '🌳'
    if level == '3':
        board_list = []
        for i in range(0,20):
            board_list.append(['🟦'] * 30)  #⬜
        board_list.insert(0, ['🌊'] * 30)
        board_list.insert(len(board_list), ['🌊'] *   30)
        for i in range(1, len(board_list) -1):
            board_list[i][0] = '🌊'
            board_list[i][-1] = '🌊'
        for i in range(0,8):
            board_list[2][i] = '🌊'
            board_list[15][10 + i] = '🌊'
            board_list[i][23] = '🌊'
            board_list[2 + i][5] = '🌊'
            board_list[8 + i][4] = '🌊'
            board_list[18][19 + i] = '🌊'
        for i in range(0,5):
            board_list[5][3 + i] = '🌊'
            board_list[10 + i][19] = '🌊'
            board_list[4][15 + i] = '🌊'
            board_list[10 + i][19] = '🌊'
            board_list[19][2 + i] = '🌊'
            board_list[4 + i][10] = '🌊'
            board_list[12][4 + i] = '🌊'     
        for i in range(0,3):
            board_list[10][26 + i] = '🌊'
            board_list[10][12 + i] = '🌊'
            board_list[10][12 + i] = '🌊'
            board_list[13 + i][25] = '🌊'
            board_list[5][3 + i] = '🌊'
            board_list[10 + i][19] = '🌊'
            board_list[6 + i][24] = '🌊'
            board_list[8 + i][15] = '🌊'
            board_list[17][2 + i] = '🌊'
    return board_list

def display_board(board):
    for sublist in board:
        print(''.join(sublist))

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