import string

restricted = string.punctuation  # !"#$%&'()*+,-./:;<=>?@[\]^_`{|}~
message = input('Введите что-то:')
counter = 0

for symbol in message:
    if symbol in restricted:
        counter += 1
print(counter)
