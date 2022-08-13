import random
import math
from math import sqrt

print('---------------------------------1----------------------------------------')
#Напишите программу, удаляющую из текста все слова, содержащие ""абв"".

with  open('f1.txt', 'r', encoding="utf-8") as file:
    for line in file:
            str =""
            tempElement = line.split(' ')
            # разбили на слова и проверяем по словам содержат ли они "абв"
            for i in range(len(tempElement)):                    
                if "абв" not in tempElement[i]:
                    str += tempElement[i]+" ";
            print( f'было: {line}')
            print( f'cтало: {str}')   

