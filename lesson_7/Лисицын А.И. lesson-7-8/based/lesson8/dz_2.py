# 2. Создайте собственный класс-исключение, обрабатывающий ситуацию деления на нуль.
# Проверьте его работу на данных, вводимых пользователем.
# При вводе пользователем нуля в качестве
# делителя программа должна корректно обработать эту ситуацию и не завершиться с ошибкой.

class Division_by_zero:
    def __init__(self, dividend, divider):
        self.dividend = dividend
        self.divider = divider

    @staticmethod
    def division_by_null(dividend, divider):
        try:
            return (dividend / divider)
        except:
            return 'Делить на ноль нельзя'


zero = Division_by_zero(100, 10)
print(Division_by_zero.division_by_null(100, 10))
print(Division_by_zero.division_by_null(0, 0))
