#На вход программе подаются две строки текста, содержащие по одному слову из перечня "камень", "ножницы", "бумага", "ящерица" или "Спок".
#На первой строке записан выбор Тимура, на второй – выбор Руслана.

#Формат выходных данных
#Программа должна вывести результат жеребьёвки: кто победил - Тимур или Руслан, или они сыграли вничью.

#Примечание. Правила игры стандартные: ножницы режут бумагу. Бумага заворачивает камень. 
#Камень давит ящерицу, а ящерица травит Спока, в то время как Спок ломает ножницы, которые, в свою очередь, отрезают голову ящерице, 
#которая ест бумагу, на которой улики против Спока.
 #Спок испаряет камень, а камень, разумеется, затупляет ножницы.

input('Введите: "камень", "ножницы", "бумага", "ящерица" или "спок"')
a=input('Выбор Руслана: ')
b=input('Выбор Тимура: ')
m = {'камень-камень': 'ничья', 
'камень-ножницы': 'Тимур', 
'камень-бумага': 'Руслан',
'камень-ящерица': 'Тимур', 
'камень-спок': 'Руслан', 
'ножницы-ножницы': 'ничья',
'ножницы-бумага': 'Тимур', 
'ножницы-камень': 'Руслан', 
'ножницы-ящерица': 'Тимур',
'ножницы-спок': 'Руслан', 
'бумага-бумага': 'ничья', 
'бумага-камень': 'Тимур',
'бумага-ножницы': 'Руслан', 
'бумага-ящерица': 'Руслан', 
'бумага-спок': 'Руслан',
'ящерица-ящерица': 'ничья', 
'ящерица-спок': 'Тимур', 
'ящерица-ножницы': 'Руслан',
'ящерица-бумага': 'Тимур', 
'ящерица-камень': 'Руслан', 
'спок-спок': 'ничья',
'спок-ножницы': 'Тимур', 
'спок-бамага': 'Руслан', 
'спок-камень': 'Тимур',
'спок-ящерица': 'Руслан'}

s=a+'-'+b

print(f'Победил: {m[s]}')