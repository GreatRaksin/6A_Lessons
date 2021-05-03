message = input('Введите что-то:').lower()
find = input('Что искать? ')
my_list = message.split()
counter = 0

for element in my_list:
    if element == find:
        counter += 1

print(counter)
