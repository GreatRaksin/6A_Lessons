'''
Сортировка списка.
Метод .sort() располагает элементы
вашего списка от меньшего к большему (или по алфавиту)
'''

cars = ['toyota', 'audi', 'volvo', 'mercedes', 'bmw']
print('Список ДО сортировки', cars)
cars.sort()
print('Список после сортировки', cars)
cars.sort(reverse=True)
print('Список после сортировки в обратном порядке', cars)