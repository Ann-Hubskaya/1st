
x = int(input('\nЗначение N  - '))
k = 2
q = 1
while k <= x:
    k *= 2
    q += 1
print('наибольшая целая степень двойки, не превосходящая степень - ', (k//2), '\nпоказатель степени - ', (q-1))



