#На колесе рулетки карманы пронумерованы от 0 до 36. Ниже приведены цвета карманов:



user_number = int(input('Введите число: '))

if user_number >= 0 and user_number <= 36:
    if user_number == 0:
        print(f'Цвет {user_number}-го кармана - зелёный')
    elif user_number >= 1 and user_number <= 10:
        if user_number % 2 == 0:
            print(f'Цвет {user_number}-го кармана - чёрный')
        else:
            print(f'Цвет {user_number}-го кармана - красный')
    elif user_number >= 11 and user_number <= 18:
        if user_number % 2 == 0:
            print(f'Цвет {user_number}-го кармана - красный')
        else:
            print(f'Цвет {user_number}-го кармана - чёрный')
    elif user_number >= 19 and user_number <= 28:
        if user_number % 2 == 0:
            print(f'Цвет {user_number}-го кармана - чёрный')
        else:
            print(f'Цвет {user_number}-го кармана - красный')
    elif user_number >= 29 and user_number <= 36:
        if user_number % 2 == 0:
            print(f'Цвет {user_number}-го кармана - красный')
        else:
            print(f'Цвет {user_number}-го кармана - чёрный')
else:
    print('Неверное число')