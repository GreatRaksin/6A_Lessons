"""Создание срезов списков"""
players = ['michelle', 'zodiac', 'michael', 'eli', 'zakhar']

print(players[:3])  # с начала до 3
# список[старт:стоп:шаг]
print(players[1:4])  # c 1 по 3 включительно
print(players[0:5:2])  # с 0 по 4 включительно ЧЕРЕЗ один
print(players[::2])  # с 0 по 4 включительно ЧЕРЕЗ один

print(players[2:])  # с индекса 2 и до конца
