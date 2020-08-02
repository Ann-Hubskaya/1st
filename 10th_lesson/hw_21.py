a = ['qwe', 25, '_the', 78523, True, 'false']


def list_revers():
    if len(a) % 2 == 0:
        i = 0
        j = len(a) - 1
        for _ in a:
            if i < j:
                a[i], a[j] = a[j], a[i]
                i += 1
                j -= 1
            return a
    else:
        i = 0
        j = len(a) - 1
        for _ in a:
            if i == len(a)-1:
                a[i], a[j] = a[j], a[i]
                i += 1
                j -= 1
            return a


list_revers()
print(a)
