'''
Author: Malek Kchaou
KUID: 3107322
Date: 09/01/2023
Lab: Lab01
Last Modified: 09/05/2023
Purpose: Class that handles data processing 
'''
from operator import itemgetter

class Game: 

    def __init__(self, file):

        self._games_data = {}
        game_data_list = []

        f = open(file, encoding = 'utf-8')
        line_count = 1

        for line in f:
            if line_count >= 2:
                game_data_list.append(line.strip('\n').split('\t'))
            line_count += 1

        for game in game_data_list:
            for i in range(len(game)):
                if i == 1:
                    game[i] = float(game[i])

        game_data_list_sorted = sorted(game_data_list, key=itemgetter(1), reverse=True)

        line_count = 2
        range_stop = 6
        for  i in range(len(game_data_list_sorted)): 
            for j in range(len(game_data_list_sorted[i])):
                self._games_data[f'game {line_count-1}'] = [game_data_list_sorted[i][j] for j in range(range_stop)]
            line_count += 1

    def get_name(self, n):
        return self._games_data[f'game {n}'][0]
    
    def get_gibbons_rating(self, n):
        return float(self._games_data[f'game {n}'][1])
    
    def get_people_avg(self, n):
        return float(self._games_data[f'game {n}'][2])
    
    def get_avg_weight(self, n):
        return float(self._games_data[f'game {n}'][3])
    
    def get_year_published(self, n):
        return int(self._games_data[f'game {n}'][4])
    
    def get_number_of_players(self, n):
        return self._games_data[f'game {n}'][5].split(',')

    def __getitem__(self, name):
        return self._games_data[name]

    def __iter__(self):
        return iter(self._games_data)

    def keys(self):
        return self._games_data.keys()

    def items(self):
        return self._games_data.items()

    def values(self):
        return self._games_data.values() 
    
     
