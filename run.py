# A board is made out of list of rows. Each row is a list of cells
# with an 'X' for a battleship or blank ' ' for water.
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

# We want to columns by letter, but because Python accesses list by
# numbers, dictionary needs to be defined, to translate letters to
# numbers.
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

print("----------------------------------")
print("WELCOME TO ULTIMATE BATTLESHIPS!!!")
print("----------------------------------")


# This fuctions lets game host choose positions of the battleships.
def ask_board_position():
    column = input("Column (A to H):").upper()
    while column not in "ABCDEFGH":
        print("Invalid column! Choose from A, B, C, D, E, F, G, H")
        column = input("Column (A to H):").upper()

    row = input("Row (1 to 8):")
    while row not in "12345678":
        print("Invalid row! Choose from 1, 2, 3, 4, 5, 6, 7, 8")
        row = input("Row (1 to 8):")

    # Code calling this function will receive values listed in return
    # statment.
    return int(row) - 1, letters_to_numbers[column]


def print_game_board(board):
    print("   A B C D E F G H")
    print("  ------------------")
    row_number = 1

    for row in board:
        print("%d|%s|" % (row_number, "|".join(row)))
        print("  ------------------")
        row_number = row_number + 1


# We want to have five battleships on our board, so for loop will ask
# for ship five times.

for n in range(5):

    print("Where do you want your ship number:", n + 1, "?")
    row_number, column_number = ask_board_position()

# This part checks if there are no repeats in the host input.
    if board[row_number][column_number] == 'X':
        print("This spot already has battleship located!")

    board[row_number][column_number] = 'X'
    print_game_board(board)

# This cleanes terminal screen, and the player can start guessing
# where game host placed his battleships.
print("\n"*40)
print("All battleships were deployed!")
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

# we will keep playing until 5 right guesses
GUESS = 0
while GUESS < 5:
    print("Guess battleship location on board")
    row_number, column_number = ask_board_position()

    if player_board[row_number][column_number] != ' ':
        print("You attacked this place!")
        continue

    if board[row_number][column_number] == 'X':
        print("You have successfully hitted the target!")
        player_board[row_number][column_number] = 'X'
        GUESS = GUESS + 1
    else:
        player_board[row_number][column_number] = '/'
        print("You have missed the target!")

    print_game_board(player_board)

print("GAME OVER! all battleships were destroyed")
print("-----------------------------------------")
