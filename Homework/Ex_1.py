#Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот день выходным.

number = int(input('Введите число: '))
if number == 6 or number == 7:
    print('Это выходной день')
elif number == 1 or number == 2 or number == 3 or number == 4 or number == 5:
    print('Это будний день')
else:
    print('Неверное число')