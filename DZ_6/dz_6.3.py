import random
import math
from math import sqrt

print('---------------------------------3----------------------------------------')
#Найти сумму чисел списка стоящих на нечетной позиции

list = [i for i in range(10)]
answer = 0
for i in range( 1, len(list),2):
    answer += list[i]
print(f'для спиcка {list} ответ {answer}'  )


