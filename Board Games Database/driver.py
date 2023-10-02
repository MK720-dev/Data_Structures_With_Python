'''
Author: Malek Kchaou
KUID: 3107322
Date: 09/01/2023
Lab: Lab01
Last Modified: 09/01/2023
Purpose: Read an input file containing data of board games and provide the user with a menu of different possible interactions
'''


from executive import Executive

def main():
    #file_name = input("Enter the name of the input file: ")
    my_exec = Executive("C:/Users/kchao/OneDrive/Documents/Dossier Malek/EECS_268/Lab1/gibbons-boardgames.tsv")
    my_exec.run()

if __name__ == "__main__":
    main()
    