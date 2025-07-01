#im coding a ludo game and this is the movement file
import stdio
import stdarray
import random

class Movement:
    def __init__(self, player, player_num):
        self.player = player
        self.position = 0
        self.player_num = player_num

    def get_move(self, player_prog):
        #cycle through each move and label correct moves
        valid_move = False
        while not valid_move:
            move = random.randint(1, 6)
            print(move)
            if (move + player_prog[self.player_num-1]) > 55:
                return 0
            valid_move = True
        return move
    
    #def add_player(self):
    #    if self.player_num == 1:
