import random


# Game board
class BattleBoard:
    def __init__(self, game_board):
        self.game_board = game_board
    # This function changes user inputed letter to numbers,
    # so it can be taken as column coordinates.

    def make_letters_to_integers():
        letters_to_integers = {
            "A": 0,
            "B": 1,
            "C": 2,
            "D": 3,
            "E": 4,
            "F": 5,
            "G": 6,
            "H": 7,
        }
        return letters_to_integers

    # This function takes care of printing game board.
    def board_print(self):
        print("  A B C D E F G H")
        print(" +-+-+-+-+-+-+-+-+")
        number_of_rows = 1
        for row in self.game_board:
            print("%d|%s|" % (number_of_rows, "|".join(row)))
            number_of_rows += 1


# Class for setting ships and taking user input.
class CreateShips:
    def __init__(self, game_board):
        self.game_board = game_board

    # This function automaticly sets 5 random ship
    # for user to guess the location of them.
    # It does that by looping throught random integers.
    # Also, checks, if place is not already taken.
    def set_ships(self):
        for i in range(5):
            self.rows, self.cols = random.randint(0, 7), random.randint(0, 7)
            while self.game_board[self.rows][self.cols] == "@":
                self.rows, self.cols = random.randint(
                    0, 7), random.randint(0, 7)
            self.game_board[self.rows][self.cols] = "@"
        return self.game_board

    # This function takes user input of the ship coordinates,
    # returns coordinates as integers.
    # Checks if user input is in the guessing range.
    # Also rejects empty input.
    def user_input(self):
        rows = input("Select row coordinates (From 1 to 8): ")
        while rows not in '12345678' or rows == "":
            print("Invalid row coordinates")
            rows = input("Select row (1 to 8): ")

        cols = input("Select column coordinates (From A to H): ").upper()
        while cols not in "ABCDEFGH" or cols == "":
            print("Invalid column coordinates")
            cols = input("Select column (A to H): ").upper()
        return int(rows) - 1, BattleBoard.make_letters_to_integers()[cols]

    # Takes username input, rejects empty input
    def user_name(self):
        name = input("Enter Your name: ").capitalize()
        while name == "":
            print("You should have a name :) ")
            name = input("Enter Your name: ").capitalize()
        return name

    # This function counts how many ships are hitted by user.
    # If users guess is right, it adds score to counter.
    def hit_counter(self):
        hitted_ships = 0
        for row in self.game_board:
            for column in row:
                if column == "@":
                    hitted_ships += 1
        return hitted_ships


def RunningGame():
    comp_board = BattleBoard([[" "] * 8 for i in range(8)])
    user_board = BattleBoard([[" "] * 8 for i in range(8)])
    # Computer sets five ships, for user to guess
    CreateShips.set_ships(comp_board)
    # Games starts when user has 15 guesses
    user_turns = 15
    print("-------------------------------")
    print("WELCOME TO ULTIMATE BATTLESHIPS")
    print("-------------------------------")
    # Taking user input, for his/hers username
    user = CreateShips.user_name(object)
    print("\n"*20)
    # Takes information from previous user input
    print(f"Hello, {user}")
    print("You have 15 shells at you disposal")
    print("You need to destroy enemy fleet, made out of 5 ships")
    print("Good luck!")
    # Game continues, until user user turns goes to 0
    while user_turns > 0:
        BattleBoard.board_print(user_board)
        # Gets user input of the ship coordinates
        user_rows, user_cols = CreateShips.user_input(object)
        # Checks if user didn't entered the same coordinates twice.
        # If user did that, requests new coordinates.
        while user_board.game_board[user_rows][user_cols] == "/" or \
                user_board.game_board[user_rows][user_cols] == "@":
            print('You already attacked these coordinates')
            user_rows, user_cols = CreateShips.user_input(object)
        # Checks if user guessed coordinates right.
        # if yes, @ simbol is paced on the board.
        if comp_board.game_board[user_rows][user_cols] == "@":
            print('You have sunk enemies ship')
            user_board.game_board[user_rows][user_cols] = "@"
        # If no, / simbol is placed on the board.
        else:
            print('You have missed the enemies ship!')
            user_board.game_board[user_rows][user_cols] = "/"
        # If user hits all five ships, winning message and game
        # and game board with all the guesses is printed, game ends.
        if CreateShips.hit_counter(user_board) == 5:
            print("\n"*20)
            print('You have destroyed enemies fleet!')
            BattleBoard.board_print(user_board)
            break
        # If user had not destroyed all ship, but still has turns:
        else:
            # Takes one turn away from user_turns
            user_turns -= 1
            print("\n"*20)
            # Shows how many turns user have left
            print(f"{user}, you have {user_turns} shells at your disposal!")
            # Shows how many ships user has hitted
            print(f"You have hitted {CreateShips.hit_counter(user_board)} \
ships out of 5")
            # If user runs out of turns, prints the message and board with
            # user guesses and ends the game
            if user_turns == 0:
                print("\n"*20)
                print('You ran out of ammunition')
                BattleBoard.board_print(user_board)
                break


if __name__ == '__main__':
    RunningGame()
