'''
Author: Malek Kchaou
KUID: 3107322
Date: 09/01/2023
Lab: Lab01
Last Modified: 09/01/2023
Purpose: Class that handles the data processing 
'''
from operator import itemgetter

class Executive:
    
    def __init__(self, file):
        
        self._Board_Games_Info = []
        f = open(file, encoding= 'utf-8')
        i = 1 
        for line in f:
            if (i >= 2):
                self._Board_Games_Info.append(line.strip('\n').split('\t'))
            i += 1 

        for games in self._Board_Games_Info:
            for i in range(len(games)):
                if i == 1:
                    games[i] = float(games[i])

        self._Board_Games_Info_sorted = sorted(self._Board_Games_Info, key=itemgetter(1), reverse=True)

        return

    def run(self):

        exit = False 

        while exit == False: 

            print('1- Print all games highest Gibbons rating to lowest')
            print('2- Print all games from a year of your choice')
            print('3- Print all games with a weight equal to or lower than weight you provide')
            print('4- The People vs Dr. Gibbons')
            print('5- Print all games based on player count')
            print('6- Exit')
            
            try:
                choice = int(input('Choose a number from 1 to 6: '))
                if choice in range(1,6):
                        if choice == 1:
                            for games in self._Board_Games_Info_sorted:
                                print('============')
                                for i in range(len(games)):
                                    print(games[i])

                        elif choice == 2: 
                            try: 
                                year = int(input('Choose a year: '))
                                game_count = 0
                                for games in self._Board_Games_Info_sorted: 
                                    for i in range(len(games)):
                                        if i==4 and int(games[4]) == year:
                                            game_count += 1
                                            print('============')
                                            for j in range(len(games)):
                                                print(games[j])
                                if game_count == 0:
                                    print('============')
                                    print('No games found')
                                print('============') 
                            except ValueError:
                                print('========================================================================')
                                print('The value you entered is not an integer!')
                                print('========================================================================')         

                        elif choice == 3: 
                            try:
                                weight = float(input('Choose a weight (float 0-5): '))
                                if (weight >= 0) and (weight <= 5):
                                    for games in self._Board_Games_Info_sorted: 
                                        for i in range(len(games)):
                                            if i==3 and float(games[3]) <= weight:
                                                print('============')
                                                for j in range(len(games)):
                                                    print(games[j])
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
                                threshhold = float(input("Input a threshhold (float 0-10) by which rating of Dr. Gibbons and people's ratings must differ: "))
                                if (threshhold >= 0) and (threshhold <= 10):
                                    for games in self._Board_Games_Info_sorted: 
                                        for i in range(len(games)):
                                            if abs(float(games[1])-float(games[2])) >= threshhold:
                                                print('============')
                                                for j in range(len(games)):
                                                    print(games[j])
                                                break
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
                                for games in self._Board_Games_Info_sorted:
                                    is_game_matching = False
                                    player_count_list = games[5].split(',') 
                                    for j in range(len(player_count_list)):
                                        if int(player_count_list[j]) == player_count:
                                            is_game_matching = True
                                            break
                                    if is_game_matching == True:
                                        print('============')
                                        for i in range(len(games)):
                                            print(games[i])
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
            
    

