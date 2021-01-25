'''a = True  # 1
b = False  # 0

# Если в переменной а содержится тру
if a > b:
    print('a is greater than b') <- будет это
else:
    print('a - ne True')
'''
ex1 = False
ex2 = False
ex3 = True
ex4 = True
mid = 4.5

if (ex1 and ex2 and ex3 and ex4) and (mid > 4):
    print('Passed!')
else:
    print('Not passed')

'''
Task 1.
Система безопасности аэропорта.
Багаж можно поместить в самолет, если 
Его ширина < 60 см,
Высота < 80 см,
Глубина < 40 cм
ИЛИ
Ширина + Высота + Глубина < 150см
'''
w = float(input('Введите ширину багажа: '))
h = float(input('Введите высоту багажа: '))
d = float(input('Введите глубину багажа: '))

if (w > 0 and h > 0 and d > 0) and ((w <= 60 and h <= 80 and d <= 40) or ((w + h + d) <= 150)):
    print('Багаж можно поместить в самолет.')
else:
    print('Ваш багаж не помещается в самолет.')