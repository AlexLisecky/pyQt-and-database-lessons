# 4. Начните работу над проектом «Склад оргтехники».
# Создайте класс, описывающий склад.
# А также класс «Оргтехника», который будет базовым для классов-наследников.
# Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс).
# В базовом классе определить параметры, общие для приведенных типов.
# В классах-наследниках реализовать параметры, уникальные для каждого типа оргтехники.
# 5. Продолжить работу над первым заданием.
# Разработать методы, отвечающие за приём оргтехники на склад и передачу в определенное подразделение компании.
# Для хранения данных о наименовании и количестве единиц оргтехники,
# а также других данных, можно использовать любую подходящую структуру, например словарь.
# 6. Продолжить работу над вторым заданием.
# Реализуйте механизм валидации вводимых пользователем данных.
# Например, для указания количества принтеров, отправленных на склад, нельзя использовать строковый тип данных.

class Org_storage:
    my_storage_full = []

    def __init__(self, name, price, pieces):
        self.name = name
        self.price = price
        self.pieces = pieces
        self.my_unit = {'Название: ': self.name, 'Цена: ': self.price, 'Количество: ': self.pieces}
        self.my_storage = []

    def __str__(self):
        return f'Название: {self.name} | Цена: {self.price} | Количество: {self.pieces}'

    def reception(self):
        try:
            unit = input(f'Введите название: ')
            unit_price = int(input(f'Введите цену за ед: '))
            unit_pieces = int(input(f'Введите количество: '))
            dct = {'Название: ': unit, 'Цена: ': unit_price, 'Количество: ': unit_pieces}
            self.my_unit.update(dct)
            self.my_storage.append(self.my_unit)
            print(f'Текущий список -\n {self.my_storage}')
        except:
            return f'Ошибка ввода данных'

        print(f'Для выхода - "Exit", продолжение - Enter')
        answer = input(': ').lower()
        if answer == "exit":
            self.my_storage_full.append(self.my_storage)
            print(f'Весь склад: {self.my_storage_full}')
            return f'Выход'
        else:
            return Org_storage.reception(self)


class Printer(Org_storage):
    def __init__(self, name, price, pieces, size):
        Org_storage.__init__(self, name, price, pieces)
        self.size = size

    def __str__(self):
        return f'Название: {self.name} | Цена: {self.price} | Количество: {self.pieces} | ' \
               f'Размер: {self.size}'


class Scaner(Org_storage):
    def __init__(self, name, price, pieces, size):
        Org_storage.__init__(self, name, price, pieces)
        self.size = size

    def __str__(self):
        return f'Название: {self.name} | Цена: {self.price} | Количество: {self.pieces} | ' \
               f'Размер: {self.size}'


class Xerox(Org_storage):
    def __init__(self, name, price, pieces, size):
        Org_storage.__init__(self, name, price, pieces)
        self.size = size

    def __str__(self):
        return f'Название: {self.name} | Цена: {self.price} | Количество: {self.pieces} | ' \
               f'Размер: {self.size}'


pos_1 = Org_storage("Samsung", 2000, 20)
pos_2 = Org_storage("HP", 3000, 10)
pos_3 = Org_storage("JW", 4000, 15)
pos_4 = Printer("DT", 5000, 10, 200)
pos_5 = Scaner("TY", 6000, 7, 150)
pos_6 = Xerox("HJ", 7000, 5, 175)

print(pos_1.reception())
print(pos_4)
print(pos_5)
print(pos_6.reception())
print(f'Весь склад: {Org_storage.my_storage_full}')
