#Задайте список из n чисел последовательности (1+1/n)**n и выведите на экран их сумму.

number = int(input('Введите число: '))
i = 1
result = []
while i <= number:
    list = round((1 + 1/i)** i, 2)
    result.append(list)
    i+=1
print((f' Последовательность: {result}'))
print(f'Сумма элиментов последовательности равна: {round(sum(result), 3)}')