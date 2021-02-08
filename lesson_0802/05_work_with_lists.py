numbers = [1, 67, 22, 13, 7, 19, 8]
'''
Для работы со списками используется цикл for.

для каждого_элемента в списке:
    сделать_что-то()
'''
for element in numbers:
    print(element)

import random
empty_list = []

for i in [1, 2, 3, 4, 5, 6]:
    empty_list.append(random.randint(-100, 100))
print(empty_list)
'''
Заполняю пустой список 6 случайными 
числами от -100 до 100.
'''
