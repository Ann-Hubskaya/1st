h = int(input('Please enter height: '))

for i in range(h):
    for j in range(h*2):
        if (
                h//2 >= i > 0 and h + i > j > h - i - 1
                or j == h - i - 1 and i <= h//2
                or i >= h//2 and i == j
                or i > h//2 and j == h*2 - 1 - i - 1 and j > h*2 - h - 1
                or j == h*2 - h - 1 and i > h // 2
             ):
            print('* ', end='')
        else:
            print('  ', end='')
    print()