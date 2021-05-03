message = input('Введите что-то: ')

if len(message) < 3:
    print(message)
# elif message[-3:] == 'ing':
elif message.endswith('ing'):
    print(message + 'ly')
else:
    print(message + 'ing')