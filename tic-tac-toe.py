# SHIVANSHU VERMA 
# BCA - KMCUAF
# 09-04-2020 :: 19:15
import os
location = {'7':' ', '8':' ', '9':' ',
            '4':' ', '5':' ', '6':' ',
            '1':' ', '2':' ', '3':' '}
 
board_keys=[]
for key in location:
    board_keys.append(key)
# Printing Game Board !!!!!!!!
def board(locations):
    line = '---'; plus = '+'
    print('\n')
    print(f"{locations['7']:^3} | {locations['8']:^3} | {locations['9']:^3}")
    print(f'{line:^3}{plus:^3}{line:^3}{plus:^3}{line:^3}')
    print(f"{locations['4']:^3} | {locations['5']:^3} | {locations['6']:^3}")
    print(f'{line:^3}{plus:^3}{line:^3}{plus:^3}{line:^3}')
    print(f"{locations['1']:^3} | {locations['2']:^3} | {locations['3']:^3}")

def CheckLocation(position):
    if location[position] == ' ':
        return True
    else:
        return False

def status(player):
    print("\n+---------------------+")
    print(f"| @@@ '{player}' : WON! @@@  |")
    print("+---------------------+\n")

def restartGame(regame):
    ''' On the Game Running time ( Mid in Game ) You want to restart than type the "r" or "R" '''
    if regame == 'r' or regame == 'R':
        return True
    else:
        return False
        
def mainGameCode():
    turn = 'X'; restart = False
    os.system('cls')
    while True:
        board(location)
        print(f"\nYour turn '{turn}', to Which place : ", end='')
        choiceinput = input()
        try:
            if restartGame(choiceinput):       
                restart = True
                os.system('cls')
                break
            if CheckLocation(choiceinput): 
                location[choiceinput] = turn    # Assign Player to the Board
                os.system('cls')
                # Here check the who win
                if location['7'] == location['8'] == location['9'] !=' ' or location['7'] == location['4'] == location['1'] !=' ' or location['4'] == location['5'] == location['6'] !=' ' or location['8'] == location['5'] == location['2'] !=' ' or location['1'] == location['2'] == location['3'] !=' 'or location['9'] == location['6'] == location['3'] !=' ' or location['1'] == location['5'] == location['9'] !=' ' or location['7'] == location['5'] == location['3'] !=' ':
                    board(location)
                    status(turn)
                    break
                elif location['1'] !=' ' and location['2'] !=' ' and location['3'] !=' ' and location['4'] !=' ' and location['5'] !=' ' and location['6'] !=' ' and location['7'] !=' ' and location['8'] !=' ' and location['9'] !=' ':
                    board(location)
                    print("\n+--------------------+")
                    print(f"|    @@@ tie @@@     |")
                    print("+--------------------+")
                    break
                # Here change the Player one by one
                if turn =='X': 
                    turn = 'O'
                else:
                    turn = 'X'
            else:
                    os.system('cls')
                    print('\n-----------------')
                    print(' Already filled.')
                    print('-----------------')
                    continue
        except KeyError:
            os.system('cls')
            print(f"Enter Only [ 1 - 9 ]")
    # Here asking to user You Want to Play Again Game!!!!!!
    if restart: 
        choice = 'y'
        for key in board_keys:
            location[key] = " "
        mainGameCode()    
    else:
        choice = input('Play Again [y/n]: ').lower()
        if choice == 'y':
            for key in board_keys:
                location[key] = " "
            os.system('cls')
            mainGameCode()    

mainGameCode()