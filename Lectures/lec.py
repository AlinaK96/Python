print('1. Проверка на кратность трём')
a = int(input("Введите число: "))
if a % 3 == 0:
    print(f"{a} кратно трём")
else:
    print(f'{a} не кратно трём')

print()
print('2. Проверка на квадрат числа')
a = int(input('ВВедите число a: '))
b = int(input('Введите число b: '))
if a**2 == b:
    print(f'{a} является квадратом {b}')
elif b**2 == a:
    print(f'{b} является квадратом {a}')
else:
    print('числа не являются квадратами друг друга')

print()
print('3. Поиск максимального в списке')

list = [1,8,9,14,75]
print(list)
max = list[0]
i = 1

while i < len(list):
    if list[i] > max:
        max = list[i]
        i+=1
print(f'Максимальное число: {max}')

print()
print('4. Напишите программу, которая будет на вход принимать число N и выводить числа от -N до N')

a = int(input('Введите число: '))
b = -a
while b <= a:
    print(b, end = ' , ')
    b+= 1
print(';')

print()
print('5. Вывод первой цифры дробной части числа')
a = float(input('Введите число: '))
b = int((a - int(a))* 10)
print(b)

print()
print('6. Напишите программу, которая проверяет, кратно ли оно 5 и 10 или 15, но не 30')
a = int(input('Введите число: '))
if (a % 5 == 0 and a % 10 == 0 or a % 15 == 0) and a % 30 != 0: 
    print('ok')
else:
    print('not ok')