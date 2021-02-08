'''
список = [2, 3, 4, "5", 6.1, "привет, Андрей!"]
'''
cars = ['audi', 'mercedes', 'bmw', 'toyota']
print(cars)

# хочу вывести 2й элемент массива !!!индексация начинается с 0!!!
print(cars[1])
print(cars[-1])  # вывести последний элемент списка
import random
print('My first car was', cars[random.randint(0, 3)])
# модуль рандом создает случайности
# randint(a, b) - выдать случайное число (random int) от а до b
print(random.randint(1, 100))

