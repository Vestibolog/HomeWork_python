import random
import math
from math import sqrt


print('---------------------------------2----------------------------------------')
#2) Задача: предложить улучшения кода для уже решённых задач с помощью использования 
# **лямбд, filter, map, zip, enumerate, list comprehension
#Дана последовательность чисел. Получить список уникальных элементов заданной последовательности.
#[1, 2, 3, 5, 1, 5, 3, 10] => [2, 10]


list = [1, 2, 3, 5, 1, 5, 3, 10]
listAnswer = [list[i] for i in range(len(list)) if (list[i] not in list[(i+1):]) and (list[i] not in list[0:(i-1)])]   
print(listAnswer)
