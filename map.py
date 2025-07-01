import stdarray
import stdio

class Map:

    def __init__(self):
        self.map = stdarray.create1D(56, ' ')
        #self.size = size

    def update_map(self, player_prog, nullPlayer, curPlayer, playerMap):
        playerMap.map[player_prog[curPlayer.player_num-1]] = nullPlayer.player
        pass

    def print(self):
        print(self.map)

    def kill(self, maps, cur_player, player_prog, players):
        #check if the current player index is the same as the other players
        for i in range(4):
            if player_prog[cur_player] > 49:
                break
            if i == cur_player:
                continue
            if player_prog[cur_player] == player_prog[i]:
                maps[i].map[player_prog[i]] = ' '
                player_prog[i] = 0
                print('Player ' + players[i].player + ' is killed by player ' + players[cur_player].player)