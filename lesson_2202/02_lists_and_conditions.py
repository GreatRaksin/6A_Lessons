numbers = [200, 345, 124, 678, 34, 16, 12, 15]

import random
numbers_rand = [random.randint(1, 100) for i in range(10)]
print(numbers_rand)  # чтобы видеть список
print('Числа больше 50:')
for number in numbers_rand: # для каждого числа в списке
    if number >= 50:  # если число больше 50
        print(number, end=' ')  # напечатать его

print()
print('Хочу вывести только четные числа, которые больше 80')
for number in numbers_rand:
    # для каждого числа в списке
    if (number % 2 == 0) and (number >= 80):
        print(number, end=' ')

print()
print('Хочу из одного списка перекинуть элементы в другой')
new_list = []
for number in numbers_rand:
    # для каждого числа в списке
    if number % 2 != 0:  # если число нечетное
        new_list.append(number)  # добавить число в другой список
print(new_list)  # вывеси новый список