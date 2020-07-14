""""""""""
Дан список целых чисел (можно сгенерировать при помощи генератора случайных чисел), число k и значение C.
Необходимо вставить в список на позицию с индексом k значение C, сдвинув все элементы, с индексом большим k, вправо.
Поскольку при этом количество элементов в списке увеличивается, в конец списка нужно будет добавить новый элемент
(любое значение), используя метод append().
Вставку необходимо осуществлять уже в считанном списке, не делая этого при выводе и не создавая доп. списка.
Использовать метод insert() не разрешается.
"""""""""""

import random

a = [random.randint(1, 50) for _ in range(15)]
print(a)
k = int(input('Please enter your number (>= 0 and <={}: - '.format(len(a)-1)))
print ('k = ', k)
C = int(input('Please enter your number C - '))

a.append(0)
for x in range(len(a)-1, k, -1):
    a[x] = a[x-1]
a[k] = C
print(a)
