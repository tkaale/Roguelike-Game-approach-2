import ui
import engine

GATE_ONE = [18,29]
INVENTORY= {'🪓': 1, '🔪': 1, '💎': 5, '🔑': 1, }

inventory_list = engine.inventory_list(INVENTORY)


def board_level_one():
    window_lst_of_lst = []
    for i in range(0,20):
        window_lst_of_lst.append(['⬛'] * 30)  #⬜
    window_lst_of_lst.insert(0, ['🧱'] * 30)
    window_lst_of_lst.insert(len(window_lst_of_lst), ['🧱'] * 30) 
    for i in range(1, len(window_lst_of_lst) -1):
        window_lst_of_lst[i][0] = '🧱'
        window_lst_of_lst[i][-1] = '🧱'
    for i in range(0,8):
        window_lst_of_lst[10][12 + i] = '🧱'
        window_lst_of_lst[13 + i][25] = '🧱'
        window_lst_of_lst[4][15 + i] = '🧱'
        window_lst_of_lst[8 + i][4] = '🧱'
        window_lst_of_lst[18][19 + i] = '🧱'
    for i in range(0,5):
        window_lst_of_lst[2][i] = '🧱'
        window_lst_of_lst[15][10 + i] = '🧱'
        window_lst_of_lst[i][23] = '🧱'
        window_lst_of_lst[2 + i][5] = '🧱'
        window_lst_of_lst[8 + i][15] = '🧱'
        window_lst_of_lst[17][2 + i] = '🧱'
        window_lst_of_lst[12][4 + i] = '🧱'
    for i in range(0,3):
        window_lst_of_lst[5][3 + i] = '🧱'
        window_lst_of_lst[10 + i][19] = '🧱'
        window_lst_of_lst[10 + i][19] = '🧱'
        window_lst_of_lst[19][2 + i] = '🧱'
        window_lst_of_lst[4 + i][10] = '🧱'
        window_lst_of_lst[10][26 + i] = '🧱'
        window_lst_of_lst[6 + i][24] = '🧱'
    ui.add_gate_to_board(window_lst_of_lst, GATE_ONE)
    window_lst_of_lst[8][8] = inventory_list[0]
    window_lst_of_lst[19][7] = inventory_list[1]
    window_lst_of_lst[16][27] = inventory_list[2]
    window_lst_of_lst[19][9] = inventory_list[3]
    window_lst_of_lst[11][6] = inventory_list[4]
    window_lst_of_lst[6][27] = inventory_list[5]
    window_lst_of_lst[16][6] = inventory_list[6]
    window_lst_of_lst[18][1] = inventory_list[7]


    return window_lst_of_lst






