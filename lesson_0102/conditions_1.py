'''Task 1.
Шахматная доска представлена черными и белыми квадратами.
Необходимо по координатам двух полей (клеток) определить,
одинаковый ли цвет у этих полей.
'''

x1 = input('Введите координату 1 клетки: ')
y1 = input('Введите координату 1 клетки: ')
x2 = input('Введите координату 2 клетки: ')
y2 = input('Введите координату 2 клетки: ')

try:
    x1 = int(x1)
    y1 = int(y1)
    x2 = int(x2)
    y2 = int(y2)

    if (x1 + y1 + x2 + y2) % 2 == 0:
        print('Клетки одинакового цвета.')
    else:
        print('Клетки разного цвета.')

except ValueError:
    print('Вы ввели не целые числа!')


