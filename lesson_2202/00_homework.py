'''1. Создать список, вывести приглашения'''
guests = ['Alice', 'Dan', 'Julia']

for name in guests:
    print('Welcome to the party,', name)

'''2. Один гость не придет. Заменить его и вывести новые приглашения'''
print(guests[2], 'can not come!')
guests[2] = 'Zodiac'
for name in guests:
    print('Welcome to the party,', name)

'''3. Добавить трех гостей '''
print()
print('#### NEW GUESTS ####')
print()
guests.insert(0, 'Alex')
guests.insert(1, 'Jack')
guests.append('Anny')

print(guests)