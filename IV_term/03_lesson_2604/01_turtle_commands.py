from turtle import *

tina = Turtle()  # создал черепашку
tina.shape('turtle')  # указал, что форма будет черепашкой
tina.speed(5)  # скорость черепашки. от 1 до 10

tina.color('yellow')  # указываю код цвета для черепашки
tina.pensize(10)  # отвечает за размер линии у черепашки
tina.fd(100)
# fd(length) - forward(length) идти вперед
tina.rt(45)
# rt(degree) - right(degree) повернуть вправо на degree градусов
tina.color('violet')
tina.pensize(5)
tina.bk(50)
# bk(length) - backward(length) идти назад
tina.color('#3eb489')
tina.lt(90)
# lt(degree) - left(degree) повернуть влево на degree градусов
tina.pensize(1)
tina.bk(100)

done()  # не даю окну закрыться сразу