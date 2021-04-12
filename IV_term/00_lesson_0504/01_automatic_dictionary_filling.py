'''Написать программу, которая создает словарь с ключами x, y, z, где значение
каждого ключа - это список из чисел 11-20, 21-30, 31-40 соответственно.
'''

dict_nums = {}

dict_nums['x'] = list(range(11, 21))
dict_nums['y'] = list(range(21, 31))
dict_nums['z'] = list(range(31, 41))

for key, value in dict_nums.items():
    print(key, ':', value)
