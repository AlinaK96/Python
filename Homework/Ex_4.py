#Напишите программу, которая по заданному номеру четверти, показывает диапазон возможных координат точек в этой четверти (x и y)

quarterNumber = int(input("Для определения диапазона возможных координат задайте номер четверти: "))

if quarterNumber == 1:
    print(f"Диапозон координанат для {quarterNumber}-ой четверти: x > 0, y > 0")
elif quarterNumber == 2:
    print(f"Диапозон координанат для {quarterNumber}-ой четверти: x < 0, y > 0")
elif quarterNumber == 3:
    print(f"Диапозон координанат для {quarterNumber}-ей четверти: x < 0, y < 0")
elif quarterNumber == 4:
    print(f"Диапозон координанат для {quarterNumber}-ой четверти: x > 0, y < 0")
else:
    print('Error')
