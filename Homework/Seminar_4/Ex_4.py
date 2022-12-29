'''
Задана натуральная степень k. 
Сформировать случайным образом список коэффициентов (значения от 0 до 100) многочлена и 
записать в файл многочлен степени k.

Пример:

- k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0
'''

import random

def write_file(name,st):
    with open(name, 'w') as data:
        data.write(st)


def rnd():
    return random.randint(0,101)