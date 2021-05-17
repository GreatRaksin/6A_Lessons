from turtle import *


def x_angle(turtle, x, y, color, length, num_of_sides):
    '''Параметры:
    turtle: черепашка, которая будет рисовать фигуру
    x, y: координаты, в которых буду рисовать фигуру
    color: цвет фигуры
    length: длина стороны
    num_of_sides: количество сторон фигуры
    '''
    turtle.up()  # сначала поднимаем перо
    turtle.goto(x, y)  # переходим в координаты, которые нам передали
    turtle.color(color)  # подставляем цвет
    turtle.down()  # начинаем рисовать
    for i in range(num_of_sides):
        turtle.fd(length)
        turtle.lt(360 / num_of_sides)
    turtle.up()  # поднимаем перо
    '''
    360 / 4 = 90
    360 / 3 = 120
    360 / 18 = 20
    360 / 6 = 60
    '''


def rectangle(turtle, x, y, color, length):
    turtle.up()  # сначала поднимаем перо
    turtle.goto(x, y)  # переходим в координаты, которые нам передали
    turtle.color(color)  # подставляем цвет
    turtle.down()  # начинаем рисовать
    for i in range(2):
        turtle.fd(length)  # длинная сторона
        turtle.lt(90)
        turtle.fd(length / 2)  # короткая сторона
        turtle.lt(90)
    turtle.up()  # поднимаем перо

tina = Turtle()  # новая черепашка
tommy = Turtle()  # еще одна черепашка

x_angle(tina, -100, 100, 'green', 50, 6)
x_angle(tommy, 50, -90, 'pink', 100, 4)
x_angle(tina, -40, 40, 'yellow', 30, 18)
x_angle(tommy, 40, 120, 'purple', 30, 5)
rectangle(tina, 0, 110, 'purple', 223)


done()