'''Task 2. Проверить, является ли список пустым или нет.'''
import random

my_list = [i for i in range(random.randint(0, 5))]
print(my_list)

# Способ 1
print('Длина списка: ', len(my_list))
# Способ 2
if not my_list:
    print('Список пуст!')
