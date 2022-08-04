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