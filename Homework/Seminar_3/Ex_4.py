'''Напишите программу, которая будет преобразовывать десятичное число в двоичное.

Пример:

- 45 -> 101101
- 3 -> 11
- 2 -> 10'''

def to_binary(number):
    result = ''
    while number > 0:
        result = str(number % 2) + result
        number = number // 2
    return result
    
number = int(input('Введите целое число: '))
print(to_binary(number))