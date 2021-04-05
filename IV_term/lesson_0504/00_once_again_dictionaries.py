school = {
    'students': [
        {'firstName': 'Jeffrey', 'lastName': 'Locker',
         'marks': {
             'math': 8,
             'physics': 9,
             'art': 6}
         },
        {'firstName': 'Sandy', 'lastName': 'Stanford',
         'marks': {
             'math': 6,
             'physics': 6,
             'art': 9}
         },
        {'firstName': 'Alice', 'lastName': 'Washington',
         'marks': {
             'math': 9,
             'physics': 9,
             'art': 9}
         }
    ],
    'teachers': [
        {'firstName': 'Clark', 'lastName': 'Southberry'},
        {'firstName': 'Amberly', 'lastName': 'Calico'},
        {'firstName': 'John', 'lastName': 'Wick'}
    ]
}
print(school['students'][0]['marks']['physics'])
# получить оценку по физике студента с индексом 0
