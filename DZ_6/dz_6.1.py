import random
import math
from math import sqrt

print('---------------------------------1----------------------------------------')
# 1) Доделать реализацию функции eval со скобками
str = "36/3+3*(5-1)"
print(eval(str))


tempArray = []
tempChar = ""
# разбиваем строку на масив
for i in str:
    if i.isdigit():
        tempChar += i
    else:
        if tempChar != "":
            tempArray.append(tempChar)
        tempArray.append(i)
        tempChar = ""
print(tempArray)

def doCalculations(i:int,value: list) -> list:
    tempChar = value[i]
    if tempChar == "*":
        tempStr = int(value[i-1]) * int(value[i+1])
    elif tempChar == "/":
        tempStr = int(value[i-1]) / int(value[i+1])
    elif tempChar == "+":
        tempStr = int(value[i-1]) + int(value[i+1])
    elif tempChar == "-":
        tempStr = int(value[i-1]) - int(value[i+1])
    else :
        print("1111111111111111111111111111")
        return []
    value.pop(i)
    value.pop(i)
    if len(value) == 0:
        value.append(tempStr)
    else:
        value[i-1] = tempStr
    print(f'{tempChar} {value}')
    return value



def calculations(value: list) -> str:
    for i in range(1, len(value) , 2):
        if i < len(value):        
            if (value[i] == "*") or (value[i] == "/"):
                value = doCalculations(i,value)

    for i in range(1, len(value) , 2):
        if i < len(value):
            if (value[i] == "+") or (value[i] == "-"):
                value = doCalculations(i,value)

    return value[0]


# раскрываем скобки. с двойными это не будет работать надо дом проверку
flag = False
inBrackets = []
i = 0
while i < len(tempArray):
    tempChar = tempArray[i]
    if tempChar == ")":
        flag = False
        print(inBrackets)
        print(calculations(inBrackets))
        tempArray[i] = calculations(inBrackets)
        print(tempArray)
    if flag:
        inBrackets.append(tempChar)
        tempArray.pop(i)
        i -= 1
    if tempChar == "(":
        flag = True
        tempArray.pop(i)
        i -= 1
    i += 1

print(f'результат  {calculations(tempArray)}')
