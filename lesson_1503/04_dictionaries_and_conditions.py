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

print('Количество дверей, объем двигателя, мощность, цвет, объем бака')
question = input('Какой параметр машины вам интересен? ').lower()
print(question)
if question == 'объем двигателя':
    print(car['engine']['volume'])
elif question == 'количество дверей':
    print(car['doors'])
elif question == 'мощность':
    print(car['engine']['power'])
elif question == 'цвет':
    print(car['color'])
else:
    raise ValueError('Такого параметра у нас нет!')
    # выдавать ошибку, если пользователь ввел что-то не того
