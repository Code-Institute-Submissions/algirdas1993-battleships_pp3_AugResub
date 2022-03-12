from random import randint

COMPUTER_BOARD = [[' '] * 8 for x in range(8)]
USER_BOARD = [[' '] * 8 for x in range(8)]


letters_to_number = {'A': 0, 'B': 1, 'C': 2, 'D': 3,
                     'E': 4, 'F': 5, 'G': 6, 'H': 7}


def print_game_board(board):
    print('   A B C D E F G H')
    print('   ---------------')
    row_number = 1
    for row in board:
        print("%d|%s|" % (row_number, "|".join(row)))
        row_number += 1

def ship_create(board):
    for ship in range(5):
        ship_row, ship_column = randint(0, 7), randint(0, 7)
        while board[ship_row][ship_column] == 'X':
            ship_row, ship_column = randint(0, 7), randint(0, 7)
        board[ship_row][ship_column] = "X"


def ship_location():
    row = input('Please enter ship row 1-8')
    while row not in '12345678':
        print('Please enter valid number')
        row = input('Please enter ship row 1-8')
    column = input('Please enter ship column A-H').upper()
    while column not in 'ABCDEFGH':
        print('Please enter valid column letter')
        column = input('Please enter ship column A-H').upper()
    return int(row) - 1, letters_to_number[column]

def count_hitted_ships():
    count = 0
    for row in board:
        for column in row:
            if column == 'X':
                count += 1
    return count            

ship_create(COMPUTER_BOARD)
turns = 10
print_game_board(COMPUTER_BOARD)
print_game_board(USER_BOARD)
# while turns > 0: