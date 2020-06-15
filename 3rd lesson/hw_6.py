
x = int(input('\nЗначение N  - '))
k = 2
q = 1
while True:
    k *= 2
    q += 1
    if (k) <= x:
        break
print(k)
print(q)
print('наибольшая целая степень двойки, не превосходящая степень - ', k, '\nпоказатель степени - ', q)


