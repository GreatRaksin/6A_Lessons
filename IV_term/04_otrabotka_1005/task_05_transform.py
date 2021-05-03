message = input('Введите что-то:')
if len(message) % 4 == 0:
    print(message[::-1])
else:
    print('Длина вашей строки не кратна 4!')