"""Копирвание списка"""

players = ['michelle', 'zodiac', 'michael',
           'eli', 'zakhar', 'jagor', 'hunter']

new_players = players[:]  # копирование
print(new_players)

another_players = []
for player in players:
    another_players.append(player)
    # тоже копирование, но более сложное
print(another_players)
