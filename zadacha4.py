#4-Напишите программу, которая по заданному номеру четверти, показывает диапазон возможных координат точек в этой четверти (x и y).
#Пример:
#quarter = 1 => x∈(0, ∞) u y∈(0,∞)

a = int(input('задайте номер четверти: '))

if a == 1:
    print("в первой четверти: x от 0 до + ∞, y от 0 до + ∞ ")
elif a == 2:
    print('во второй четверти: x от 0 до  - ∞, y от 0  до + ∞ ')
elif a == 3:
    print('в третьей четверти: x от 0 до  - ∞, y от 0  до - ∞ ')
elif a == 4:
    print('в четвертой четверти: x от 0 до  + ∞, y от 0  до - ∞ ')
else:
    print('такой четверти нет')