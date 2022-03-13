board = [
    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
]

letters_to_numbers = {
    'A': 0,
    'B': 1,
    'C': 2,
    'D': 3,
    'E': 4,
    'F': 5,
    'G': 6,
    'H': 7,
}


def ask_board_position():
    column = input("Column (A to H):").upper()
    while column not in "ABCDEFGH":
        print("Invalid column! Choose from A, B, C, D, E, F, G, H")
        column = input("Column (A to H):").upper()

    row = input("Row (1 to 8):")
    while row not in "12345678":
        print("Invalid row! Choose from 1, 2, 3, 4, 5, 6, 7, 8")
        row = input("Row (1 to 8):")
    return int(row) - 1, letters_to_numbers[column]

def print_game_board(board):
    print(" A B C D E F G H")
    print(" ---------------")
    row_number = 1
    for row in board:
        print("%d|%s|" % (row_number, "|".join(row)))
        print(" ---------------")
        row_number = row_number + 1


for n in range(5):
    print("Where do you want your ship ", n + 1, "?")
    row_number, column_number = ask_board_position()

    if board[row_number][column_number] == 'X':
        print("This spot already has battleship!")

    board[row_number][column_number] = 'X'
    print_game_board(board)


print("\n"*60)

player_board = [
    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
]


guess = 0
while guess < 5:
    print("Guess battleship location on board")
    row_number, column_number = ask_board_position()

    if player_board[row_number][column_number] != ' ':
        print("You attacked this place!")
        continue

    if board[row_number][column_number] == 'X':
        print("You have successfully hitted the target")
        player_board[row_number][column_number] = 'X'
        guess = guess + 1
    else:
        player_board[row_number][column_number] = '/'
        print("You have missed the target!")

    print_game_board(player_board)
print("GAME OVER")