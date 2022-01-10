# 1. Написать функцию host_ping(), в которой с помощью утилиты ping будет проверяться доступность сетевых узлов.
# Аргументом функции является список, в котором каждый сетевой узел должен быть представлен именем хоста или ip-адресом.
# В функции необходимо перебирать ip-адреса и проверять их доступность с выводом соответствующего сообщения
# («Узел доступен», «Узел недоступен»). При этом ip-адрес сетевого узла должен создаваться с помощью функции
# ip_address().


from ipaddress import ip_address
import subprocess


def host_ping(list_ip_address):
    # новый словарь со списками для хранения проверенных адресов
    checked_address = {'Узел доступен:': [],
                       'Узел недоступен:': []}
    # перебираю списко Ip-адресов
    for address in list_ip_address:
        address = ip_address(address)
        print(f'Обрабатываю адрес {str(address)}...')
        PROCESS = subprocess.Popen(f'ping {address}', shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        CODE = PROCESS.wait()
        # проверка кода ответа
        if CODE == 0:
            checked_address['Узел доступен:'].append(str(address))
            print(f'Адрес {str(address)} доступен')
        else:
            checked_address['Узел недоступен:'].append(str(address))
            print(f'Адрес {str(address)} недоступен')
    print(f'Общая информация по адресам {checked_address}')
    return checked_address


if __name__ == '__main__':
    lst_ip_address = ["192.168.0.1", "0.0.0.0", "108.177.14.100"]
    host_ping(lst_ip_address)
