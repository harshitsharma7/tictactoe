

class TicTacToe:
    def __init__(self):
        self.board = [" " for x in range(3) for y in range(3)]
        self.current_winner = None

    def print_board(self):
        for row in range(3):
            print("| " + " | ")