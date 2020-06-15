a = int(input('Class math_1 size is '))
b = int(input('Class math_2 size is '))
c = int(input('Class math_3 size is '))
print('\n')
x = a + b + c
if a > 0 and b > 0 and c > 0:
    if (x % 2) > 0:
        print('You need to buy', (x // 2) + 1, 'desks')
    else:
        print('You need to buy', x // 2, 'desks')
else:
    print('Please enter correct data')
