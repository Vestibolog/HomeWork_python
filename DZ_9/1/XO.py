import random
import math
from math import sqrt



print('---------------------------------3----------------------------------------')
#Создайте программу для игры в ""Крестики-нолики"".



array = [" . "," . "," . "," . "," . "," . "," . "," . "," . ",]
flagInGame = False
mainArray = ["1","2","3","4","5","6","7","8","9",]

#array = mainArray.copy()

def ptintArray(array: list) :
    print()
    for i in range(0,3):
            print(f'{array[0+i*3]}  {array[1+i*3]}  {array[2+i*3]}  ')

ptintArray(array)

def playerTurn() :
    print(f'ваш ход. Выбирете сколько число 0<X<9')
    tempInt = int(input())
    if (0 <= tempInt < 9) and ( array[tempInt] == " . " ):
        array[tempInt] = "X"
        mainArray[tempInt] = "X"
    else:
        print(f'!!!! некоректное значение')
        playerTurn()

def botTurn() :
    tempInt  = random.randint(0, 9)
    if (0 <= tempInt < 9) and ( array[tempInt] == " . " ):
        array[tempInt] = "0"
        mainArray[tempInt] = "0"
    else:
        botTurn()

def winnercheck()-> bool:
    flag = False
    for i in range(0,3):
        if array[0+i*3] == array[1+i*3] == array[2+i*3] != " . ":
            flag = True

    for i in range(0,3):
        if array[i+0*3] == array[i+1*3] == array[i+2*3] != " . ":
            flag = True
    if array[0] == array[4] == array[8] != " . ":
        flag = True        
    if array[2] == array[4] == array[6] != " . ":
        flag = True        
    return flag



#while " . " in array:
#   playerTurn()
#    if winnercheck() :
#        print("вы победили !!!!!!!!")
#        break
#    botTurn()
#    if winnercheck() :
#        print("вы проиграли !!!!!!!!")
#        break




print('---------------------------------TEL----------------------------------------')
def XO_gameIter(value:int) ->str :
    global flagInGame
    if not flagInGame :
        return XO_startGame()
    tempStr = ""
    if (0 <= value < 9) and ( array[value] == " . " ):
        array[value] = "X"
        mainArray[value] = "X"
        tempStr += arrayToStr(array)
        if winnercheck() :
            tempStr +=" вы победили !!!!!!!!\n"
            tempStr +="Еще разок ? \n"
            return tempStr;

        botTurn()
        if winnercheck() :
            tempStr +="вы проиграли !!!!!!!! \n"
            tempStr +="Еще разок ? \n"
            flagInGame = false
            return tempStr
        
        tempStr += "\n ход противника \n"
        tempStr += arrayToStr(array)

        if " . " not in array:
            tempStr +="Ничья !!!!!!!! \n"
            tempStr +="Еще разок ? \n"
            flagInGame = false
            return tempStr

        tempStr += "ваш ход. Выбирете сколько число 0<X<9"        
    else:
        tempStr = '!!!! некоректное значение'
    return tempStr;



def XO_startGame() ->str :
    global flagInGame
    array = [" . "," . "," . "," . "," . "," . "," . "," . "," . ",]
    tempStr = "Начинаем игру \n"
    flagInGame = True
    if (random.randint(0, 1) == 0):
        botTurn()

    tempStr = "ваш ход. Выбирете сколько число 0<X<9"
    tempStr += arrayToStr(array)
    return tempStr;

def arrayToStr(value :array) ->str :
    tempStr = "";
    for i in range(len(value)):
        tempStr += value[i]
        if ( (i+1)%3 == 0 ):
            tempStr += "\n"
    return tempStr;


print(XO_startGame())