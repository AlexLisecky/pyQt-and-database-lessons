# 2. Реализовать проект расчета суммарного расхода ткани на производство одежды.
# Основная сущность (класс) этого проекта — одежда, которая может иметь определенное название.
# К типам одежды в этом проекте относятся пальто и костюм.
# У этих типов одежды существуют параметры: размер (для пальто) и рост (для костюма).
# Это могут быть обычные числа: V и H, соответственно.
# Для определения расхода ткани по каждому типу одежды использовать формулы:
# для пальто (V/6.5 + 0.5), для костюма (2 * H + 0.3).
# Проверить работу этих методов на реальных данных.
# Реализовать общий подсчет расхода ткани.
# Проверить на практике полученные на этом уроке знания:
# реализовать абстрактные классы для основных классов проекта,
# проверить на практике работу декоратора @property.

class Clothen:
    def __init__(self, v, h):
        self.v = v
        self.h = h

    def coat(self):
        return self.v / 6.5 + 0.5

    def jacket(self):
        return 2 * self.h + 0.3

    @property
    def summ(self):
        return (self.v / 6.5 + 0.5) + (2 * self.h + 0.3)


class Coat(Clothen):
    def __init__(self, v, h):
        super().__init__(v, h)
        self.coat_result = round(self.v / 6.5 + 0.5)

    def __str__(self):
        return f'Площадь на пальто {self.coat_result}'


class Jacket(Clothen):
    def __init__(self, v, h):
        super().__init__(v, h)
        self.jacket_result = round(self.h * 2 + 0.3)

    def __str__(self):
        return f'Площадь на костюм {self.jacket_result}'


coat = Coat(100, 50)
jacket = Jacket(100, 50)
print(coat)
print(jacket)
print(coat.summ)
print(jacket.jacket_result)
