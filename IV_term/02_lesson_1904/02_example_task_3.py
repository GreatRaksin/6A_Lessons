'''Проверить, является ли введенная строка палиндромом.
Палиндром - это слово, которое одинаково читается
слева-направо и справа-налево'''
message = input('Введите что-то: ').strip()

print(message == message[::-1])
