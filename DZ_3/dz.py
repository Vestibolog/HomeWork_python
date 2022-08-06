import random
import math

print('---------------------------------1----------------------------------------')
# Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.
# [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

list = [2, 3, 5, 9, 3]


def sumOfOdd(value: list) -> int:
    tempInt = 0
    if (len(value) >= 2):
        for i in range(1, len(value), 2):
            print(f'i={i} элемент {value[i]}')
            tempInt += value[i]
    return tempInt


print(f'для массива {list} ответ {sumOfOdd(list)}')

print('---------------------------------2----------------------------------------')
# Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# [2, 3, 4, 5, 6] => [12, 15, 16];
# [2, 3, 5, 6] => [12, 15]
list = [2, 3, 4, 5, 6]
#list = [2, 3,  5, 6];


def sumPair(value: list) -> list:
    tempList = []
    if (len(value) >= 2):
        for i in range(0, int(len(value)/2+0.5), 1):
            tempList.append(value[i]*value[len(value)-1-i])
    return tempList


print(f'для массива {list} ответ {sumPair(list)}')

print('---------------------------------3----------------------------------------')
# Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.
# [1.1, 1.2, 3.1, 5, 10.01] => 0.19

list = [1.1, 1.2, 3.1, 5, 10.01]


def subtractMaxMin(value: list) -> int:
    tempMin = 0
    tempMax = 0
    for i in range(0, len(value), 1):
        # если убрать окгругление отсет будет 0.199999999
        tempNum = round(value[i] - int(value[i]), 2)
        if (tempMin > tempNum):
            tempMin = tempNum
        if (tempMax < tempNum):
            tempMax = tempNum
            print(f'----tempMax = {tempMax}')
    print(f'tempMin = {tempMin}')
    print(f'tempMax = {tempMax}')
    return tempMax - tempMin


print(f'для массива {list} ответ {subtractMaxMin(list)}')


print('---------------------------------4----------------------------------------')
# Напишите программу, которая будет преобразовывать десятичное число в двоичное.
# 45 -> 101101
# 3 -> 11
# # 2 -> 10

num = 45


def toBinary(value: int) -> str:
    tempStr = ''
    while value >= 1:
        print(f'{value}  {value//2}  {value%2}')
        tempStr = str(value % 2) + tempStr
        value //= 2
    return tempStr


print(f'чисто {num} в двоичном {toBinary(num)}')

print('---------------------------------5----------------------------------------')
# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
# для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21] [Негафибоначчи]

num = 8

# без рекурсии тут вызовов можно было бы сделать меньше. То так как это у нас часть курса оставл.
def fibonacci(value: int) -> int:
    if value == 0:
        return 0;
    elif value == 1:
        return 1
    else:
        return fibonacci(value-1)+fibonacci(value-2)


tempList = []
for i in range(-num, num+1, 1):
    if (i < 0):
        tempList.append(fibonacci(-i)*(-1**(-i)))
    else:
        tempList.append(fibonacci(i))


print(f'для числа  {num} ответ {tempList}')
