message = input('Введите что-то:')
restricted = ',.;:!?'
counter = 0

for symbol in restricted:
    counter += message.count(symbol)

print(counter)

