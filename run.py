import random


class BattleBoard:
    def __init__(self, game_board):
        self.game_board = game_board

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

    def board_print(self):
        print("A B C D E F G H")
        print("+-+-+-+-+-+-+-+")
        number_of_rows = 1
        for row in self.game_board:
            print("%d|%s|" % (number_of_rows, "|".join(row)))
            number_of_rows += 1

class CreateShips:
    def __init__(self, game_board):
        self.game_board = game_board

    def set_ships(self):
        for i in range(5):
            self.rows, self.cols = random.randint(0, 7), random.randint(0, 7)
            while self.game_board[self.rows][self.cols] == "@":
                self.rows, self.cols = random.randint(0, 7), random.randint(0, 7)
            self.game_board[self.rows][self.cols] = "@"
        return self.game_board

    def user_input(self):
        cols = input("Select column (A to H): ").upper()
        while cols not in "ABCDEFGH":
            print("Invalid column")
            cols = input("Select column (A to H): ").upper()

        rows = int(input("Select row (1 to 8): "))
        while rows not in "12345678":
            print("Invalid row")
            rows = int(input("Select row (1 to 8): "))
        return self.BattleBoard.make_letters_to_integers()[cols], self.rows - 1

    def hit_counter(self):
        hitted_ships = 0
        for row in self.game_board:
            for column in row:
                if column == "@":
                    hitted_ships += 1
        return hitted_ships 

         