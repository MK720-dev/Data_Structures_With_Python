'''
Author: Malek Kchaou
KUID: 3107322
Date: 09/01/2023
Lab: Lab01
Last Modified: 09/05/2023
Purpose: Read an input file containing data of board games and provide the user with a menu of different possible interactions
'''


from executive1 import Executive1

def main():
    file_name = input("Enter the name of the input file: ")
    my_exec = Executive1(file_name)
    my_exec.run()

if __name__ == "__main__":
    main()