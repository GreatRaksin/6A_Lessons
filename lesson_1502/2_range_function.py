list1 = list(range(30))
# простое создание списка из 30 чисел, числа от 0 до 29(!!!)
print(list1)

squares = []
for value in range(1, 11):
    square = value ** 2
    # переменная квадрат - возвожу каждое число из промежутка во вторую степень
    squares.append(square)
    # добавляю получившееся число в список
print(squares)