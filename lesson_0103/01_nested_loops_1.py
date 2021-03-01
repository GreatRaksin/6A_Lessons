stars = int(input('Сколько звезд нужно? '))
lines = int(input('Сколько линий нужно? '))
blocks = int(input('Сколько блоков нужно? '))

for block in range(1, blocks + 1):  # генерирую блоки
    print('Блок №', block)  # пишем номер блока
    for line in range(1, lines + 1):  # генерирую линии
        for star in range(1, stars + 1):  # генерирую звездочки
            print('*', end=' ')
        print('Линия №', line)  # пишем номер линии
    print()