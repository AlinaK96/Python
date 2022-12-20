'''Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.

Пример:

- [2, 3, 4, 5, 6] => [12, 15, 16];
- [2, 3, 5, 6] => [12, 15] '''

import random

n = int(input('Введите количество элиментов списка: '))


numbers = list(random.randint(1, 10) for _ in range(n))

print(f'Первоначальный список: {numbers}')
result = [numbers[i] * numbers[len(numbers) - 1 - i] for i in range(int(len(numbers)/2))]
print(f'Произведение пар: {result}')