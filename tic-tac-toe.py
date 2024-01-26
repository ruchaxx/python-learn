def display_board(board_list):
    print(board_list[0]+'|'+board_list[1]+'|'+board_list[2])
    print("-----")
    print(board_list[3]+'|'+board_list[4]+'|'+board_list[5])
    print("-----")
    print(board_list[6]+'|'+board_list[7]+'|'+board_list[8])


board_list = ['','','','','','','','','']

display_board(board_list)

choice = 'o'
def user_input():
    choice = input("select your choice x or o:  ")
    print("player1 will be "+choice)
    return choice

board_index = ''
def replace_value_player1():
    board_index = input("player1 select index possition from 1-9: ")
    board_list[int(board_index)-1] = 'x'
    display_board(board_list)

def replace_value_player2():
    board_index = input("player2 select index possition from 1-9: ")
    board_list[int(board_index)-1] = 'o'
    display_board(board_list)

choice = user_input()

want_to_play = 'y'

print("\nchoice ",choice)

while want_to_play == 'y':
    if choice == 'x':
        replace_value_player1()
        replace_value_player2()
    elif choice == 'o':
        replace_value_player2()
        replace_value_player1()
    want_to_play = input("do u want to play(y/n): ")

def win_logic(board_list):
    for i in board_list:
        pass

