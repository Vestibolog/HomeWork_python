import random
import math
from math import sqrt



print('---------------------------------3----------------------------------------')
#Создайте программу для игры в ""Крестики-нолики"".

array = [".",".",".",".",".",".",".",".",".",]

def ptintArray(array: list) :
    print()
    for i in range(0,3):
            print(f'{array[0+i*3]}  {array[1+i*3]}  {array[2+i*3]}  ')

ptintArray(array)

def playerTurn() :
    print(f'ваш ход. Выбирете сколько число 0<X<9')
    tempInt = int(input())
    if (0 <= tempInt < 9) and ( array[tempInt] == "." ):
        array[tempInt] = "X"
        ptintArray(array)
    else:
        print(f'!!!! некоректное значение')
        playerTurn()

def botTurn() :
    tempInt  = random.randint(0, 9)
    if (0 <= tempInt < 9) and ( array[tempInt] == "." ):
        array[tempInt] = "0"
        ptintArray(array)
    else:
        botTurn()

def winnercheck()-> bool:
    flag = False
    for i in range(0,3):
        if array[0+i*3] == array[1+i*3] == array[2+i*3] != ".":
            flag = True

    for i in range(0,3):
        if array[i+0*3] == array[i+1*3] == array[i+2*3] != ".":
            flag = True
    if array[0] == array[4] == array[8] != ".":
        flag = True        
    if array[2] == array[4] == array[6] != ".":
        flag = True        
    return flag

if (random.randint(0, 1) == 0):
    botTurn()

while "." in array:
    playerTurn()
    if winnercheck() :
        print("вы победили !!!!!!!!")
        break
    botTurn()
    if winnercheck() :
        print("вы проиграли !!!!!!!!")
        break