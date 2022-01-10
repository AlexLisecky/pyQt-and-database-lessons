# 3. Написать функцию host_range_ping_tab(), возможности которой основаны на функции из примера 2.
# Но в данном случае результат должен быть итоговым по всем ip-адресам, представленным в табличном формате
# (использовать модуль tabulate). Таблица должна состоять из двух колонок и выглядеть примерно так:


from tabulate import tabulate
import task_2


def host_range_ping_tab():
    lst_tabulate = task_2.host_range_ping()

    print(tabulate(lst_tabulate, headers='keys'))


host_range_ping_tab()
