#Создайте функцию, принимающую на вход 3 числа и возвращающую наибольшее из ниx

#numbers = []
#    number = int(input('Введите число: '))
#    numbers.append(number)
#print(numbers)
#print(f' Максимальное число: {max(numbers)}')

#Создайте функцию, принимающую на вход имя, возраст и город проживания человека.
#Функция должна возвращать строку вида «Василий, 21 год(а), проживает в городе Москва»

							
#def person_info(name, age, city):
#    result =f'{name}, {age} год(а), проживает в городе {city}'
#    return result

#print(person_info('Василий', '21', 'Москва'))

player_1 = input('Введите имя первого игрока: ')
player = {'Игрок 1': {player_1}, 'health': 100, 'damage':50}

player_2 = input('Введите имя второго игрока: ')
enemy = {'Игрок 2': {player_2}, 'health': 50, 'damage':30}		
print(player)
print(enemy)

def game (init, target):
    target ['health'] -= init ['damage']


game(player, enemy)
print(enemy)
print(player)