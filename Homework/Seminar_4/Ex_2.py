'''
Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.
48 - 2, 2, 2, 2, 3
'''

number = int(input("Введите число: "))
i = 2  
list = []
old = number
while i <= number:
    if number % i == 0:
        list.append(i)
        number //= i
        i = 2
    else:
        i += 1
print(f"Простые множители числа {old} приведены в списке: {list}")