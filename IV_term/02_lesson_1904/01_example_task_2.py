'''Task 2. Проверить, что слово начинается и заканчивается
на одну и ту же букву. Например:
---> сос
---> True

---> c
---> False (!!!)
'''
message = input('Введите что-то: ').strip()  # сразу убираю возможные пробелы
# заводим переменную для получения сообщения
if len(message) <= 1:
    print('Введите больше одной буквы!')
else:
    print(message[0] == message[-1])