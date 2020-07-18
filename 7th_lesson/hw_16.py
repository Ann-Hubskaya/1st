'''''''''
ДЗ 16. Функцию is_year_leap
Написать функцию is_year_leap, принимающую 1 аргумент — год, и возвращающую True, если год високосный, и False иначе.
'''''''''


def is_year_leap(year):
    if year % 4 == 0 and year % 100 != 0 and year % 400 != 0 or (year % 100 == 0 and year % 400 == 0):
        print(True)
    else:
        print(False)


year = int(input('Enter year(>0) - '))
is_year_leap(year)
