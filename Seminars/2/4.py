'''1. Напишите программу, которая принимает на вход число N и выдаёт последовательность из N членов.

*Пример:*

- Для N = 5: 1, -3, 9, -27, 81'''

number = int(input('Введите число: '))

for i in range(number):
    if i % 2 != 0:
        print(-3 ** i,end=" ")
    else:
        print(3 ** i,end=" ")