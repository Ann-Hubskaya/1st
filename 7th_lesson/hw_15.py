"""""
ДЗ 15. Функцию arithmetic
Написать функцию arithmetic, принимающую 3 аргумента: первые 2 - числа, третий - операция, которая должна быть 
произведена над ними. Функция должна вернуть результат вычислений зависящий от третьего аргумент +, сложить их; если -,
то вычесть; * — умножить; / — разделить (первое на второе). В остальных случаях вернуть строку "Неизвестная операция".
"""""


def arithmetic(first_number, second_number, arg):
    if arg == '+':
        res = first_number + second_number
    elif arg == '-':
        res = first_number - second_number
    elif arg == '*':
        res = first_number * second_number
    elif arg == '/':
        res = first_number / second_number
    else:
        res = 'Неизвестная операция'
    return res

first_number = int(input('Первое число - '))
second_number = int(input('Второе число - '))
arg = input('Аргумент - ')

print('Результат - ', arithmetic(first_number, second_number, arg))

arithmetic(first_number, second_number, arg)