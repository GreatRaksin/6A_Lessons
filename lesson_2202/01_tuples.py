'''Кортежи - это то же самое, что список(массив),
только в круглых скобках и не способно изменяться.
'''

dimension = (200, 50)  # кортеж
dimension2 = [200, 50]  # список/массив

try:
    dimension.pop()
except:
    print('Удалять элементы нельзя!')

print('Хочу перебрать элементы кортежа')
for element in dimension:
    print(element)

dimension = (500, 100)
print('Новый кортеж')
for element in dimension:
    print(element)