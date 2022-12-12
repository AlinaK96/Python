#Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве.
#Пример:
# A (3,6); B (2,1) -> 5,09
#- A (7,-5); B (1,-1) -> 7,21
# sqrt {(x2-x1) ^{2} + (y2-y1) ^{2}} 

import math

x1 = float(input('x1 = '))
y1 = float(input('y1 = '))
x2 = float(input('x2 = '))
y2 = float(input('y2 = '))

print(f'Координаты точек: ({x1},{y1}); ({x2}, {y2})')

distance = math.sqrt(pow(x2 - x1, 2) + pow(y2 - y1, 2))
dis = round(distance,2)
print(dis)
