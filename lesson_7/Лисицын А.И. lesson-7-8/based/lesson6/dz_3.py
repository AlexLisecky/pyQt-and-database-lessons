# 3. Реализовать базовый класс Worker (работник),
# в котором определить атрибуты: name, surname, position (должность), income (доход).
# Последний атрибут должен быть защищенным и ссылаться на словарь, содержащий элементы:
# оклад и премия, например, {"wage": wage, "bonus": bonus}.
# Создать класс Position (должность) на базе класса Worker.
# В классе Position реализовать методы получения полного имени сотрудника
# (get_full_name) и дохода с учетом премии (get_total_income).
# Проверить работу примера на реальных данных
# (создать экземпляры класса Position, передать данные, проверить значения атрибутов,
# вызвать методы экземпляров).

class Worker:
    def __init__(self, name, surname, position, pay, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {'income': pay, 'bonus': bonus}


class Position(Worker):
    def __init__(self, name, surname, position, pay, bonus):
        super().__init__(name, surname, position, pay, bonus)

    def get_full_name(self):
        return 'Ф.И.О сотрудника ' + self.name + ' ' + self.surname

    def get_total_income(self):
        return f'Доход сотрудника : {sum(self._income.values())}'


status = Position('Alex', 'Lisecky', 'Student', 50000, 10000)
print(status.get_full_name())
print(status.get_total_income())
