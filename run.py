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
        try:
            rows = input("Select row (1 to 8): ")
            while rows not in '12345678' or rows == "":
                print("Invalid row")
                rows = input("Select row (1 to 8): ")

            cols = input("Select column (A to H): ").upper()
            while cols not in "ABCDEFGH" or cols == "":
                print("Invalid column")
                cols = input("Select column (A to H): ").upper()
            return int(rows) - 1, BattleBoard.make_letters_to_integers()[cols]
        except KeyError and ValueError:
            print('Sorry, You choosen invalid coordinates')
            return self.user_input()

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
    CreateShips.set_ships(comp_board)
    user_turns = 15
    while user_turns > 0:
        BattleBoard.board_print(user_board)
        BattleBoard.board_print(comp_board)
        user_rows, user_cols = CreateShips.user_input(object)
        while user_board.game_board[user_rows][user_cols] == "/" or user_board.game_board[user_rows][user_cols] == "@":
            print('You already attacked those coordinates')
            user_rows, user_cols = CreateShips.user_input(object)
            if comp_board.game_board[user_rows][user_cols] == "@":
                print('You have sunk enemies ship')
                user_board.game_board[user_rows][user_cols] = "@"
            else:
                print('You have missed the enemy!')
                user_board.game_board[user_rows][user_cols] = "/"
        if CreateShips.hit_counter(user_board) == 5:
            print('You have destroyed enemies fleet!')
            break
        else:
            user_turns -= 1
            print(f"You have {user_turns} shells at your disposal!")
            if user_turns == 0:
                print('You run out of ammunition')
                BattleBoard.board_print(user_board)
                break


if __name__ == '__main__':
    RunningGame()