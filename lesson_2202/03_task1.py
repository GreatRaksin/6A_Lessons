'''Task 1. Найти целые числа в списке.
Дан список num_list, необходимо найти все
целые числа и перенести их в список new_list
'''
num_list = [2, 1.25, 0.56, 4, 5.56, 5.0, 13, 1.4, 78]
new_list = []

for element in num_list:
    if type(element) == int:
        new_list.append(element)

print(new_list)
