import random
import math
from math import sqrt


print('---------------------------------4----------------------------------------')
# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.

myStr = "WWWWWWWWWBBBWWWWWWWWWWWWWWWWWWWWWWWWBWWWWWWWWWWWWWW"
print(f'изначальная строка {myStr}')

def cutDown(value: str) -> str:
    tempStr = ""
    tempInt = 0
    currentLetter = ""
    for i in range(len(value)):
        tempLetter = value[i]
        if currentLetter != tempLetter:
            if tempInt != 0:
                tempStr += str(tempInt) + currentLetter
            currentLetter = tempLetter
            tempInt = 1
        else :
            tempInt += 1
    if tempInt != 0:
        tempStr += str(tempInt) + currentLetter
        currentLetter = tempLetter
    return tempStr

myStr = cutDown(myStr)
print(f'в архив {myStr}')

def expand(value: str) -> str:
    tempStr = ""
    tempInt = 0
    currentLetter = ""
    for i in range(len(value)):
        if value[i] in ["0","1","2","3","4","5","6","7","8","9"]:
            currentLetter += value[i]
        else :
            for j in range(int(currentLetter)):
                tempStr += value[i]
            currentLetter =""
        
    return tempStr

myStr = expand(myStr)
print(f'из архив {myStr}')