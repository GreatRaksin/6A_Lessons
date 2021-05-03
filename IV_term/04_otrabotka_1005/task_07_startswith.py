message = input('Введите что-то:').lower().strip()
find = input('Что будем искать? ').lower().strip()

print(message.startswith(find))