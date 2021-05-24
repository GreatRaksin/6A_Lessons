# <- это однострочный комментарий
'''
Это многострочный
'''
_varriable1 = 5

if 2 + 2 == 4:
    print(True)
elif 2 + 2 == 5:
    print('durachok')
else:
    print(False)


# and, or, not
"""
login = input()
password = input()
if login == 'Architect' and password == '23r9834y':
    print('Hello')
else:
    print('Goodbye')"""

# for - работает определенное количество раз
# while - работает по условию
for i in range(1, 11):
    # каскадное условие
    if i == 3:
        print('Пропускаю')
        continue  # пропускает повторение
    elif i == 8:
        print('Я все')
        break  # выход из цикла
    else:
        print(f'Итерация №{i}')


print(int('5') + 10)  # преобразовываю в целое число
print(float('2.5') + 0.034)  # преобразовываю в дробь
print(str(6) + 'a')  # преобразовываю в строку
