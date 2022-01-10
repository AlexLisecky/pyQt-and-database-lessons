# 2. Написать функцию host_range_ping() для перебора ip-адресов из заданного диапазона.
# Меняться должен только последний октет каждого адреса. По результатам проверки должно выводиться
# соответствующее сообщение

import task_1
from ipaddress import ip_address


# started_ip = ip_address('108.177.14.255')


def host_range_ping():
    #валидация входных данных
    try:
        started_ip = ip_address(input('Введите стартовый ip_address'))
        ip_range = int(input('Сколько адресов проверить?'))
    except ValueError:
        print('Неверно задан стартовый ip_address или диапозон')
        ip_range = 0
    if ip_range:
        # пустой списко для проверки
        lst_need_to_check = []
        #цикл перебокри ip адресов,путем прибавления по 1 к октету
        for i in range(ip_range):
            ip_division = str(started_ip).split('.')
            if ip_division[3] == '255':
                lst_need_to_check.append(str(started_ip))
                print('Неверено указанный диапазон\nПроверяю возможные адреса')
                break
            lst_need_to_check.append(str(started_ip))
            started_ip += 1
        print(f'Адреса данные на проверку{lst_need_to_check}')
        # импорт функции задания 1
        return task_1.host_ping(lst_need_to_check)


if __name__== "__main__":
    host_range_ping()
