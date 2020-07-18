"""""
ДЗ 18. Функцию season

Написать функцию season, принимающую 1 аргумент — номер месяца (от 1 до 12), и возвращающую время года, 
которому этот месяц принадлежит (зима, весна, лето или осень).
"""""


def season(month_number):
    if month_number >=3 and month_number <= 5:
        res = "весна"
    elif month_number >= 6 and month_number <= 8:
        res = "лето"
    elif month_number >= 6 and month_number <= 11:
        res = "осень"
    else:
        res = "зима"
    return res


month_number = int(input('Enter month_number(>0 and <=12) - '))
print(season(month_number))
season(month_number)