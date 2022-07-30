import random
import math

print('-------------------------------------------------------------------------');
#Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
#  6782 -> 23
# 0,56 -> 11
num = 0,56
myString = str(num)
result = 0
for value in myString:
    if 48 <= ord(value) <= 58:
        result += int(value)
print(f'у числа {num} сумма {result}');

print('-------------------------------------------------------------------------');
#Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.
# пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)

N = 4
result = []
tempNum =1;
for i in range(1,N+1):
    tempNum *= i;
    result.append(tempNum)
print(f'у числа {N} ответ {result}');  

print('-------------------------------------------------------------------------');
#Задайте список из n чисел последовательности (1+1/n)^n и выведите на экран их сумму.
#Для n = 6: {1: 4, 2: 7, 3: 10, 4: 13, 5: 16, 6: 19}
N = 6
myArray = []
result = 0;
for i in range(1 , N+1):
    tempVal = (1+1/i)**i
    myArray.append( tempVal )
    result += tempVal
print(myArray)
print(f'сумма указанных элементов = {result}');  

print('-------------------------------------------------------------------------');
#Задайте список из N элементов, заполненных числами из промежутка [-N, N]. Найдите произведение элементов на указанных позициях. Позиции хранятся в файле file.txt 
# в одной строке одно число.
N = 10;
myArray = []
result = 0
for i in range(-N , N+1):
    myArray.append(i)
print(myArray)
data = open('./file.txt', 'r')
for line in data:
    print(f'элемент {line} = {myArray[int(line)]}');  
    result +=myArray[int(line)]
data.close()
print(f'сумма указанных элементов = {result}');  

print('-------------------------------------------------------------------------');
#Реализуйте алгоритм перемешивания списка.

myArray = ["a","b","c","d","e","f"]
result = []
print(f'изначальный список = {myArray}');  
for i in range(0 , len(myArray)):
    temp = random.randint(0, len(myArray)-1)
    tempVal = myArray[ temp ]
    result.append(tempVal)
    myArray.remove(tempVal)
print(f'список после сортировки = {result}');  
