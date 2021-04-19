'''Task 4. Вводится строка. Убрать из строки знаки препинания.
[in]---> Привет, Андрей!
[out]---> Привет Андрей
'''
import string  # библиотека для работы со строками

restricted = string.punctuation + ' '
# метод punctuation возвращает все знаки препинания, добавляю к ним пробел
message = input('Введите что-то: ').strip().lower()

for symbol in restricted:
    message = message.replace(symbol, '')

print(message)
