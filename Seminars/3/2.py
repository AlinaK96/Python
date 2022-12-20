'''
2)Орел и решка

Формат выходных данных
Программа должна вывести наибольшее количество подряд выпавших Решек.

Тестовые данные
Sample Input 1:
ОРРОРОРООРРРО
Sample Output 1:
3
Sample Input 2:
ООООООРРРОРОРРРРРРР
Sample Output 2:
7
Sample Input 3:
ООООРРРРОРОРРРРРРРРООРОРОРРРРРРРРРРРРРРРРРРРРРРРРРРРРРРР
Sample Output 3:
31'''


string = input('Введите текст: ')
search = "Р"
count = 0

while string.count(search) > 0:
    count+=1
    search+= 'Р'
print(count)