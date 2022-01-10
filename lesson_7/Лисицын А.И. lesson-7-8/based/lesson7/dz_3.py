class Cell:
    def __init__(self, result):
        self.result = int(result)

    def __str__(self):
        return f'result {self.result * "*"}'

    def __add__(self, other):
        return Cell(self.result + other.result)

    def __sub__(self, other):
        return (self.result - other.result) if ((self.result - other.result) > 0) else print('Число ушло в минус')

    def __mul__(self, other):
        return Cell(int(self.result * other.result))

    def __truediv__(self, other):
        return Cell(round(self.result // other.result))

    def make_order(self, road):
        row = ''
        for i in range(int(self.result / road)):
            row += f'{"*" * road} \\n'
        row += f'{"*" * (self.result % road)}'
        return row


cells1 = Cell(50)
cells2 = Cell(15)
print(cells1 + cells2)
print(cells1 - cells2)
print(cells1 * cells2)
print(cells1 / cells2)
print(cells2.make_order(10))
print(cells1.make_order(13))
