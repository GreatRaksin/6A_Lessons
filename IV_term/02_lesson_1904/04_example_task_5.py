'''Task 5. Вводится строка. Необходимо достать
из нее все числа. И поместить их в список'''
message = input('Введите что-то: ').strip()
nums = []
for symbol in message:
    if symbol.isdigit():
        nums.append(symbol)

print(nums)
