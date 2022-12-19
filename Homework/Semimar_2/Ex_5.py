#Реализуйте алгоритм перемешивания списка. (рандомно поменять местами элементы списка между собой)

import random
list = []

number = int(input('Введите количество элиментов: '))
random.seed
for i in range(number):
    list.append(random.randint(-100, 100))
print(f'Список элиментов {list}')

random.shuffle(list)
print(f'Новый список: {list}')