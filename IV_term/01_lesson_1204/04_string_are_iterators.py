for letter in 'hello':
    print(letter.upper())

phone = input('Введите номер телефона: ')
restricted = '+()- ,.!'
clean_number = ''

for symbol in phone:
    if symbol not in restricted:
        clean_number += symbol
print(clean_number)