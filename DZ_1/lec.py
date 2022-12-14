print('-------------------------------------------------------------------------');
#1. Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот день выходным.
#Пример:
#- 6 -> да
#- 7 -> да
#- 1 -> нет

print('ввидите число - день недели');
day = int(input())
if 6 <= day <= 7:
    print(f'{day} - это выходной день');
elif  1 <= day <= 5:
    print(f'{day} - это обычный день');
else  :
    print(f'{day} - это не номер дня недели');

print('-------------------------------------------------------------------------');
#Напишите программу для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.
list = [[0,0,0],[0,0,1],[0,1,0],[0,1,1],[1,0,0],[1,0,1],[1,1,0],[1,1,1]]
lambda_left = lambda value: not( value[0] or value[1] or value[2])
lambda_right = lambda value: not value[0] and not value[1] and not value[2]

for data in list:
    print(f'{data} - {lambda_left(data)} - {lambda_right(data)}');

print('-------------------------------------------------------------------------');
#Напишите программу, которая принимает на вход координаты точки (X и Y), причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости, в которой находится эта точка (или на какой оси она находится).
#- x=34; y=-30 -> 4
#- x=2; y=4-> 1
#- x=-34; y=-30 -> 3

point_x = 2
point_y = 4
if point_x > 0 and point_y > 0:
    print(f'точка ({point_x};{point_y}) - в первой четверти');
elif point_x < 0 and point_y > 0:
    print(f'точка ({point_x};{point_y}) - во второй четверти');
elif point_x < 0 and point_y < 0:
    print(f'точка ({point_x};{point_y}) - в третий четверти');
elif point_x > 0 and point_y < 0:
    print(f'точка ({point_x};{point_y}) - в четрертой четверти');
else: 
    print(f'точка ({point_x};{point_y}) - начало координат');


print('-------------------------------------------------------------------------');
#Напишите программу, которая по заданному номеру четверти, показывает диапазон возможных координат точек в этой четверти (x и y).
number = 3
if number % 4 == 1:
    print(f'для первой четверти x из (0,∞]  y из (0,∞]');
elif number % 4 == 2:
    print(f'для второй четверти x из [-∞,0)  y из (0,∞]');
elif number % 4 == 3:
    print(f'для третий четверти x из [-∞,0)  y из [-∞,0)');
elif number % 4 == 0:
    print(f'для четвертой четверти x из (0,∞]   y из [-∞,0)');

print('-------------------------------------------------------------------------');
#Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве.
#- A (3,6); B (2,1) -> 5,09
#- A (7,-5); B (1,-1) -> 7,21

point_a = [7,-5]
point_b = [1,-1]
print( ((point_a[0] - point_b[0])**2 + (point_a[1] - point_b[1])**2) ** (0.5) );

print('-------------------------------------------------------------------------');
#найти факториал числа
n = 10
factarial =1;
for num in range(1,n+1):
    factarial *= num
print(f'{n} факториал - {factarial} ');

