print('count A  B \t A and B   A or B')
count = 1
for a in [0, 1]:
    for b in [0, 1]:
        print('#', count, end='')
        print('\t ', a, ' ', b, ' \t ', a and b, '\t ', a or b)
        count += 1