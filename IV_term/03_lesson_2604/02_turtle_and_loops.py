from turtle import *

tina = Turtle()
tina.shape('turtle')

# квадрат
for side in range(4):
    tina.fd(100)
    tina.rt(90)

# треугольник
for side in range(3):
    tina.fd(100)
    tina.lt(120)

# прямоугольник
for side in range(2):
    tina.fd(100)
    tina.rt(90)
    tina.fd(50)
    tina.rt(90)

# круг
tina.speed(0)
for i in range(180):
    tina.fd(1)
    tina.rt(1)

done()
