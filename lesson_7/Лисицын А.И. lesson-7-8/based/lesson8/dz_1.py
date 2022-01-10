# 1. Реализовать класс «Дата», функция-конструктор которого должна принимать
# дату в виде строки формата «день-месяц-год».
# В рамках класса реализовать два метода.
# Первый, с декоратором @classmethod, должен извлекать число, месяц, год и преобразовывать их тип к типу «Число».
# Второй, с декоратором @staticmethod, должен проводить валидацию числа, месяца и года (например, месяц — от 1 до 12).
# Проверить работу полученной структуры на реальных данных.


class Data:
    def __init__(self, user_data):
        self.user_data = str(user_data)

    @classmethod
    def ext(cls, user_data):
        my_list = []

        for i in user_data.split():
            if i != '-': my_list.append(i)

        return int(my_list[0]), int(my_list[1]), int(my_list[2])

    def __str__(self):
        return f'Дата на текущий момент: {Data.ext(self.user_data)}'

    @staticmethod
    def check(day, month, year):
        if (1 < day < 31) and (1 < month < 12) and (0 <= year <= 2020):
            return 'Все верно'
        else:
            return 'Неправильная дата'


a = Data("10 - 20 - 2020")
print(a)
print(Data.check(11, 12, 2200))
print(a.check(10, 10, 2019))
print(Data.ext('11 - 25 - 2020'))
print(a.ext('11 - 15 - 1000'))
