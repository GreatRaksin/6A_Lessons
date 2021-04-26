from turtle import *

tina = Turtle()  # создал черепашку
s = Screen()  # создаю переменную экрана
s.bgcolor('black')  # указываю цвет фона

register_shape('turtle.gif')  # регистрация новой формы
tina.shape('turtle.gif')  # применение новой формы
tina.color('#ffffff')


tina.fd(100)
tina.lt(90)
tina.fd(100)

# flaticon.com

done()  # не даю окну закрыться сразу