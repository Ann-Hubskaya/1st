h = int(input('Please enter height: '))

for i in range(h):
    for j in range(h*2):
        if (
                i > 0 and h + i > j > h - i - 1
                or j == h - i - 1
             ):
            print('* ', end='')
        else:
            print('  ', end='')
    print()