""""
Написать функцию для перевода десятичного числа в другую систему исчисления (2-36).  
Небольшая подсказка. В этой задаче вам может понадобиться:
 - список
 - метод `revers()` (или срез [::-1], или вместо `revers()` использовать `insert()` тогда не придётся разворачивать 
список), чтоб развернуть список, метод `join()`
 - строка `ascii_uppercase` из модуля `string` (её можно получить если сделать импорт 
`from string import ascii_uppercase`), она содержит все буквы латинского алфавита.
""" ""

from string import ascii_uppercase
from string import digits

a = int(input('Введите число: '))
b = int(input('Введите систему счисления: '))


def convert(a, b):
    s = digits + ascii_uppercase
    if a < b:
        return s[a]
    else:
        return convert(a // b, b) + s[a % b]


print(convert(a, b))
