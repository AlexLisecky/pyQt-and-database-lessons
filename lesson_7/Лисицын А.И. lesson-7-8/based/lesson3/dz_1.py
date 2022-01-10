# 1. Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление.
# Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль.

"""def my_func():
    arg_1 = float(input('Введите число которое хотите поделить: '))
    arg_2 = float(input('На какое число делить?: '))
    division = arg_1 / arg_2
    return round(division, 2)


print(my_func())
"""


def clone_func():
    """Функция деления запрашиваемых аргументов"""
    try:
        arg_1 = int(input('Введите число которое хотите поделить: '))
        arg_2 = int(input('На какое число делить?: '))
        division = arg_1 / arg_2
        return round(division, 2)
    except ZeroDivisionError:
        return ("На ноль делить нельзя")
    except ValueError:
        return ("Введите число")


print((clone_func()))
