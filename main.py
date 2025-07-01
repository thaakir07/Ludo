import stdio
import stdarray
import random
import sys
from map import Map
from movement import Movement

def main():
    redMap = Map()
    blueMap = Map()
    greenMap = Map()
    yellowMap = Map()
    redPlayer = Movement("R", 1)
    bluePlayer = Movement("B", 2)
    greenPlayer = Movement("G", 3)
    yellowPlayer = Movement("Y", 4)
    maps = [redMap, blueMap, greenMap, yellowMap]
    players = [redPlayer, bluePlayer, greenPlayer, yellowPlayer]
    game(maps, players)


def game(maps, players):
    num_cur_players = [1, 1, 1, 1]
    cur_player = 0
    game_over = False
    player_prog = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
    nulPlayer = Movement(" ", 5)
    
    while not game_over:
        move = players[cur_player].get_move(player_prog)
        if move == 6:
            choice = input("Do you want to bring a token out of home? (y/n): ")
            if choice == 'y':
                num_cur_players[cur_player] += 1
                new_token = Movement(players[cur_player].player, num_cur_players[cur_player])
                maps[cur_player].update_map(player_prog[cur_player][players[cur_player].player_num-1], players[cur_player], players[cur_player], maps[cur_player])

        maps[cur_player].update_map(player_prog, nulPlayer, players[cur_player], maps[cur_player])
        
        player_prog[cur_player] += move
        maps[cur_player].update_map(player_prog, players[cur_player], players[cur_player], maps[cur_player])
        
        maps[cur_player].kill(maps, cur_player, player_prog, players)

        maps[cur_player].print()
        print('\n')
        game_over = game_status(player_prog, players[cur_player], cur_player)

        #if cur_player < 3:
        #    cur_player += 1
        #else:
        #    cur_player = 0

    sys.exit()

def game_status(player_prog, players, cur_player):
    if player_prog[cur_player] == 55:
        return True
    return False
    

if __name__ == '__main__': main()