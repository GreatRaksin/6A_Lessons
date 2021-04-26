from turtle import *

tina = Turtle()  # создал черепашку
tina.shape('turtle')  # указал, что форма будет черепашкой

tina.fd(100)
# fd(length) - forward(length) идти вперед
tina.rt(45)
# rt(degree) - right(degree) повернуть вправо на degree градусов
tina.bk(50)
# bk(length) - backward(length) идти назад
tina.lt(90)
# lt(degree) - left(degree) повернуть влево на degree градусов
tina.bk(100)

done()  # не даю окну закрыться сразу