numbers = {
    0: 'zero', 1: 'one', 2: 'two', 3: 'three',
    4: 'four', 5: 'five', 6: 'six', 7: 'seven',
    8: 'eight', 9: 'nine',
}

number = int(input('Введите цифру:'))
if number not in numbers:
    print('Такой цифры нет!')
else:
    print(numbers[number])