'''Добавление ключей выполняется следующим образом:
название_словаря['новый_ключ'] = 'новое_значение'
'''

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
# хочу добавить параметр "объем багажника"
car['trunk_volume'] = 350
print(car)

# чтобы заменить значение
car['engine']['volume'] = 4.2
print(car['engine'])

# чтобы удалить пару ключ-значение
del car['doors']  # удалил двери
print(car)
