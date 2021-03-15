car = {
    'color': ['black', 'golden'],
    'doors': 4,
    'engine': {
        'volume': 3.5,
        'power': 170,
        'consumption': 11,
    },
    'fuel': 100,
    'tank_capacity': 120,
}

# вывести все ключи из словаря .keys()
for key in car.keys():
    print(key)
print()
# вывести все значения из словаря .values()
for value in car.values():
    print(value)
print()

# Вывести все вместе .items() - помните про 2 переменные в цикле:
for key, value in car.items():
    print('Key: ', key)
    print('Value: ', value)