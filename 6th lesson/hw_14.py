# Даны два списка чисел (можно сгенерировать при помощи генератора случайных чисел).
# Посчитайте, сколько уникальных чисел содержится одновременно как в первом списке, так и во втором.
# Примечание. Эту задачу можно решить в одну строчку.

import random
res = len((set([random.randint(1, 12) for _ in range(10)])^set([random.randint(1, 12) for _ in range(10)])))
print(res)

# a = [random.randint(1, 12) for _ in range(10)]
# b = [random.randint(1, 12) for _ in range(10)]
# print(a)
# print(b)
# c = set(a)
# print(c)
# d = set(b)
# print(d)
# print((c^d))
# print(len(c^d))
