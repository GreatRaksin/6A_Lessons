squares_1 = []
for value in range(1, 11):
    square = value ** 2
    squares_1.append(square)
print(squares_1)

squares_2 = [value ** 2 for value in range(1, 11)]
print(squares_2)