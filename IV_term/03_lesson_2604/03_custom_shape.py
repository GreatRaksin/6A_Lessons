from turtle import *
from random import choice

tina = Turtle()  # создал черепашку
s = Screen()  # создаю переменную экрана
s.bgcolor('black')  # указываю цвет фона

register_shape('turtle.gif')  # регистрация новой формы
tina.shape('turtle.gif')  # применение новой формы
tina.color('#ffffff')

colors = ['#ffff00', '#666600', '#e09d3f', '#ffc0cb',
          '#fa9284', '#45f235', '#d8ebd1', '#ff00ff', '#42aaff']
step = 10  # сколько шагов идти
size = 2  # размер пера
for side in range(400):
    tina.color(choice(colors))
    tina.fd(step)
    tina.left(90)  # если менять угол, будут получаться красивые штуки
    tina.pensize(size)
    step += 10
    size += 0.01

done()  # не даю окну закрыться сразу