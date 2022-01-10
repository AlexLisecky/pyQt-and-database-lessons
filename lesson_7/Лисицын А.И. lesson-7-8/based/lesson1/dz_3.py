"""
Модуль запрашивает число от 1 до 9 и выдает сумму формата x + xx + xxx.
"""

number = int(input("Введите число: "))

first = number

two = str(number) + str(number)

three = str(number) + str(number) + str(number)

_sum = int(first) + int(two) + int(three)

print(_sum)
