'''Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.

Пример:

- для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1,  1, 1, 2, 3, 5, 8, 13, 21]'''

n = int(input('Задайте число: '))
def fib(n):
    if n in [1, 2]:
        return 1
    else:
        return fib (n - 1) + fib (n - 2)

list = []
for i in range (1, n):
    list.append(-fib(i)) 
    list.append(fib(i)) 

list.sort()
print(list)