message = input('Введите что-то:')
counter = 0

for letter in message[:4]:
    if letter.isupper():
        counter += 1
if counter >= 2:
    print(message.upper())