'''Базовые методы изменения строк'''

name = '    Demid Raksin  '
print(name)
print(name.strip())
'''
.rstrip() - пробел справа
.lstrip() - пробел слева
.strip() - убрать пробелы с обеих сторон

.upper() - сделать все буквы большими
.lower() - сделать все буквы маленькими

.replace(a, b) - заменить символ а на символ b

.count(x) - получить количество символов х в строке
.index(x) - определить порядковый номер символа x в строке
'''
m_str = 'krice'
print(m_str.replace('kri', 'lol'))

phrase = 'Привет, Андрей, зачем ты плюнул в голубей?'
print(phrase.count('е'))
print(phrase.index('?'))