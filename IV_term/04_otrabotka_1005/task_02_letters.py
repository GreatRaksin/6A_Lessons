message = input('Введите что-то:')
if len(message) <= 2:
    pass
else:
    print(message[:2] + message[-2:])