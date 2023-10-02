'''
Author: Malek Kchaou
KUID: 3107322
Date: 09/01/2023
Lab: Lab01
Last Modified: 09/07/2023
Purpose: Class that defines what the different menu options do 
'''

from game import Game

class Executive1:
    
    def __init__(self, file):
        self._games = Game(file)

    def run(self):

        exit = False 

        while exit == False: 

            print('1- Print all games highest Gibbons rating to lowest')
            print('2- Print all games from a year of your choice')
            print('3- Print all games with a weight equal to or lower than weight you provide')
            print('4- The People vs Dr. Gibbons')
            print('5- Print all games based on player count')
            print('6- Exit ')
            
            i = iter(self._games)

            try:
                choice = int(input('Choose a number from 1 to 6: '))
                if choice in range(1,6):
                        if choice == 1:
                            for i in self._games:
                                print('============')
                                for j in range(len(self._games[i])):
                                    print(self._games[i][j])
                            print('============')
                        elif choice == 2: 
                            try: 
                                year = int(input('Choose a year: '))
                                game_count = 1
                                same_year_game_count = 0
                                for i in self._games: 
                                    if self._games.get_year_published(game_count) == year:
                                        same_year_game_count += 1
                                        print('============')
                                        for j in range(len(self._games[i])):
                                            print(self._games[i][j])
                                    game_count += 1
                                if same_year_game_count == 0:
                                    print('============')
                                    print('No games found!')
                                print('============') 
                            except ValueError:
                                print('========================================================================')
                                print('The value you entered is not an integer!')
                                print('========================================================================')         
                        
                        elif choice == 3: 
                            try:
                                weight = float(input('Choose a weight (float 0-5): '))
                                if (weight >= 0) and (weight <= 5):
                                    game_count = 1
                                    for i in self._games: 
                                        if self._games.get_avg_weight(game_count) <= weight:
                                            print('============')
                                            for j in range(len(self._games[i])):
                                                print(self._games[i][j])
                                        game_count += 1
                                    print('============')
                                else:
                                    print('========================================================================')
                                    print('The value you entered is not a float between 0 and 5!')
                                    print('========================================================================')   
                            except ValueError:
                                print('========================================================================')
                                print('The value you entered is not a float!')
                                print('========================================================================')       
  
                        elif choice == 4:
                            try:
                                threshhold = float(input("Input a threshhold (float 0-10) by which rating of Dr. Gibbons and people's rating must differ: "))
                                game_count = 1
                                games_ge_thresh = 0
                                if (threshhold >= 0) and (threshhold <= 10):
                                    for i in self._games: 
                                        if abs(self._games.get_gibbons_rating(game_count)-self._games.get_people_avg(game_count)) >= threshhold:
                                            games_ge_thresh += 1
                                            print('============')
                                            for j in range(len(self._games[i])):
                                                print(self._games[i][j])
                                        game_count += 1

                                    if (games_ge_thresh == 0):
                                        print('========================================================================')
                                        print('No games found with that threshhold!')
                                        print('========================================================================')
                                    
                                    else:
                                        print('============')
                                    
                                else: 
                                    print('========================================================================')
                                    print('The value you entered is not a float between 0 and 10!')
                                    print('========================================================================')

                                    
                            except ValueError:
                                print('========================================================================')
                                print('The value you entered is not a float!')
                                print('========================================================================')
                        
                        elif choice == 5:
                            try:
                                player_count = int(input('Please enter a player count: '))
                                game_count = 1
                                matching_games = 0
                                for i in self._games:
                                    is_game_matching = False
                                    player_count_list = self._games.get_number_of_players(game_count)
                                    for j in range(len(player_count_list)):
                                        if int(player_count_list[j]) == player_count:
                                            is_game_matching = True
                                            matching_games += 1
                                            break
                                    if is_game_matching == True:
                                        print('============')
                                        for k in range(len(self._games[i])):
                                            print(self._games[i][k])
                                    game_count += 1

                                if matching_games == 0:
                                    print('========================================================================')
                                    print('No games found with that player count!')
                                    print('========================================================================')
                                else:
                                    print('============')

                            except ValueError:
                                print('========================================================================')
                                print('The value you entered is not an integer!')
                                print('========================================================================')
                elif choice == 6:
                    print('Exiting...')
                    break    
                  

                else:
                    print('========================================================================')
                    print("The option you chose isn't on the list. The number SHOULD be an integer from 1 to 6!")
                    print('========================================================================')
            except ValueError:
                print('========================================================================')
                print('The value you entered is not an integer!')
                print('========================================================================')
        return