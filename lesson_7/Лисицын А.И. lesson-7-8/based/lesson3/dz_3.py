# 3. Реализовать функцию my_func(), которая принимает три позиционных аргумента,
# и возвращает сумму наибольших двух аргументов.

def sum_max_number(arg_1, arg_2, arg_3):
    """Функция возвращает сумму наибольших двух аргументов"""
    min_number = min(arg_1, arg_2, arg_3)
    args = min([arg_1, arg_2, arg_3])
    args.remove(min_number)
    print(sum(args))


sum_max_number(10, 15, 20)
# РЕЗУЛЬТАТ '35'
