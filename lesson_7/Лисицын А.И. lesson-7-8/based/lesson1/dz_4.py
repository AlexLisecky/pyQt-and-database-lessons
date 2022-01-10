"""
Модуль запрашиваюший число и выдает максимальную цифру в числе.
"""
number = int(input("Введите целое положительное число: "))
_max = 0

while number > 0:
    last = number % 10
    number = number // 10
    if last > _max:
        _max = last

print(_max)
