''' Задайте список из N элементов, заполненных числами из промежутка [-N, N]. Найдите произведение элементов на указанных позициях. 
Позиции хранятся в отдельном списке( пример n=4, lst1=[4,-2,1,3] - списко на основе n, а позиции элементов lst2=[3,1].'''

import random

number = int(input('Введите количество элиментов: '))
if number <= 0:
    print('Некорректный ввод')
else:
    list=[]
    random.seed
    for i in range(number):
        list.append(random.randint(-number, number))
    print(f'Список элиментов {list}')

listpos = []
position1 = int(input('Введите первую позицию для подсчёта произведения: '))
position2 = int(input('Введите вторую позицию для подсчёта произведения: '))
listpos.append(position1)
listpos.append(position2)

result = list[(position1 - 1)] * list[(position2 - 1)]
print(f'Произведение элиментов на позициях {listpos} равно: {result}')