# Даны два списка чисел (можно сгенерировать при помощи генератора случайных чисел).
# Посчитайте, сколько уникальных чисел содержится одновременно как в первом списке, так и во втором.
# Примечание. Эту задачу можно решить в одну строчку.

import random
res = len(set([random.randint(1, 12) for _ in range(10)]+[random.randint(1, 12) for _ in range(10)]))
print(res)