import random
import math
from math import sqrt

print('---------------------------------1----------------------------------------')
# Вычислить число pi c заданной точностью d Пример:
# - при $d = 0.001, π = 3.141.$    $10^{-1} ≤ d ≤10^{-10}$

d = 0.001
prevPi = 0
n = 0
pi = 4
while (int(prevPi / d) - int(pi / d)) != 0:
    prevPi = pi
    n += 1
    pi += 4*(-1)**n / (2*n+1)
    # print(pi)
print(f'pi с точностью {d} нашли за {n} шагов и оно равно {int(pi/d)*d}')


print('---------------------------------2----------------------------------------')
# Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.
N = 60
tempN = N
list = set()
for i in range(2, int(sqrt(N))+1):
    while (tempN % i == 0):
        list.add(i)
        tempN /= i
print(f'Число {N} состоит из {list}')

print('---------------------------------3----------------------------------------')
# Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.

list = ["qwe", "qwe", "a", "aa", "aa", "asd", "asd", "asd"]
tempList = set(list)
listAnswer = []
for word in tempList:
    listAnswer.append(word)


print(f'список {list} без повторов привратиться в {listAnswer}')

print('---------------------------------4----------------------------------------')
# Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от 0 до 100) многочлена и записать в файл многочлен степени k.
# k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0

k = 5
strAnswer = f'{random.randint(1, 100)}*x^{k}'
for i in range(k -1 ,0,-1):
    tenpINt = random.randint(0, 100)
    if ( tenpINt !=0 ):
        strAnswer += f' + {tenpINt}*x^{i}'
tenpINt = random.randint(0, 100)    
if ( tenpINt !=0 ):
    strAnswer += f' + {tenpINt}'
strAnswer += ' = 0'
print( strAnswer)

print('---------------------------------4----------------------------------------')
# Даны два файла, в каждом из которых находится запись многочлена. Задача - сформировать файл, содержащий сумму многочленов.


def fileToList(value: str) -> list:
    tempList =[]
    data = open(value, 'r')
    for line in data:
        print(line)
        tempArr = line.split(' ')
        #print(tempArr )

        max = 0;
        for i in range(len(tempArr)):
            if '*x^' in tempArr[i]:
                tempElement = tempArr[i].split('*x^')
                if max < int(tempElement[1]):
                    max = int(tempElement[1]);
        for n in range(max+1):            
            tempList.append(0)

        for i in range(len(tempArr)-1,-1,-1):
            if '*x^' in tempArr[i]:
                tempElement = tempArr[i].split('*x^')
                #print(tempElement[1])
                tempList[int(tempElement[1])] = tempElement[0]
    data.close()
    return tempList

list1  = fileToList('./f1.txt')
list2  = fileToList('./f2.txt')
listAnswer =[]

for i in range(len(list1)):
    listAnswer.append(int( list1[i] ) +  int( list2[i] ))

strAnswer =""
for i in range( len(listAnswer)-1 ,-1,-1):
    tenpINt = listAnswer[i]
    if ( tenpINt !=0 ):
        strAnswer += f' + {tenpINt}*x^{i}'
strAnswer += ' = 0'
data = open('sumf1f2.txt', 'a')
data.writelines(strAnswer)
data.close()
print( f'сумма многочленов {strAnswer}')


print('---------------------------------5----------------------------------------')
# 1. Создать текстовый файл (не программно). Построчно записать фамилии сотрудников и величину их окладов (не менее 10 строк). Определить, кто из сотрудников имеет оклад менее 20 тысяч, 
# вывести фамилии этих сотрудников. Выполнить подсчёт средней величины дохода сотрудников.
# Иванов 23543.12
# Петров 13749.32

totalSalary = 0
numberEmployees =0

data = open('fio.txt', 'r', encoding="utf-8")
for line in data:
    tempElement = line.split(' ')
    if len( tempElement ) == 2:
        tempNum = float( tempElement[1] )
        numberEmployees +=1
        totalSalary += tempNum
        if tempNum > 20000:
            print(tempElement[0])
    else:
        print('наккоректные данные')
data.close()
print('')
print(f'Всего сотрудников {numberEmployees}')
print(f'Средняя ЗП  {totalSalary/numberEmployees}')

print('---------------------------------6----------------------------------------')
# В файле находится N натуральных чисел, записанных через пробел. Среди чисел не хватает одного, чтобы выполнялось условие A[i] - 1 = A[i-1]. Найти его.
