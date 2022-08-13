import random
import math
from math import sqrt

print('---------------------------------2----------------------------------------')
# Создайте программу для игры с конфетами человек против человека.
# Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга. Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет.
# Все конфеты оппонента достаются сделавшему последний ход. Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?
# a) Добавьте игру против бота
# b) Подумайте как наделить бота ""интеллектом""

candies = 221

if (random.randint(0, 1) == 0):
    print("ваш ход. Выбирете сколько конвет вы возмете 1<X<28, если вы укажете некоректное число будет считаться что вы взяли одну")
    tempInt = int(input())
    if 1 < tempInt < 28:
        candies -= tempInt
    else:
        candies -= 1
    print(f'осталось  {candies} конфет')
while candies > 0:
    tempMin = min(28,candies)
    tempInt = random.randint(0, tempMin)

    #делаем немного поумнее
    if candies<28:
        tempInt = candies
    else:
        tempInt = candies %28 -1
    print(f'бот взял  {tempInt} конфет')
    candies -= tempInt
    print(f'осталось  {candies} конфет')
    if candies == 0:
        print(f'победил бот !!!!!!!')
        break
    print(f'ваш ход. Выбирете сколько конвет вы возмете 1<X<{tempMin}, если вы укажете некоректное число будет считаться что вы взяли одну')
    tempInt = int(input())
    if 1 < tempInt < tempMin:
        candies -= tempInt
    else:
        candies -= 1
    print(f'осталось  {candies} конфет')
    if candies == 0:
        print(f'победили вы !!!!!!!')
        break