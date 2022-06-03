import math
import random

class Player:
    def __init__(self, letter):
        # letter is x or o
        self.letter = letter

    def get_move(self, game):
        pass

class RandomComputerPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self, game):
        return random.choice(game.available_moves())

class HumanPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self, game):
        valid_move = False
        val = None
        while not valid_move:
            square = input(self.letter + '\'s turn. Input move 0:9')

            try:
                val = int(square)
                if val not in game.available_moves():
                    raise ValueError
                valid_move = True
            except ValueError:
                print("Please retry with a valid move.")

        return val
