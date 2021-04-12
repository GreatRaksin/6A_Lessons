name = input('Введите имя: ').title()

print(f'Привет, {name}!')

amount = float(input('Сколько денег нужно? '))
years = float(input('На сколько лет? '))
perc = float(input('Процентная ставка: '))
res = ((amount * (perc / 100)) + amount) * years
print(f'При сумме {amount}, за {years} лет вы заплатите {res} руб.')
