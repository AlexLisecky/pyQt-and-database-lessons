# 4. Реализуйте базовый класс Car.
# У данного класса должны быть следующие атрибуты: speed, color, name, is_police (булево).
# А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась, повернула (куда).
# Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar.
# Добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля.
# Для классов TownCar и WorkCar переопределите метод show_speed.
# При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
# Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат.
# Выполните вызов методов и также покажите результат.

class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print(f'Автомобиль {self.name} поехал')

    def stop(self):
        print(f'Автомобиль {self.name} остановился')

    def turn_left(self):
        print(f'Автомобиль {self.name} повернул налево')

    def turn_right(self):
        print(f'Автомобиль {self.name} повернул направо')

    def show_speed(self):
        print(f'Автомобиль {self.name} движется со скоростью {self.speed} ')


class TownCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        print(f'Автомобиль {self.name} движется со скоростью {self.speed} ')
        if self.speed > 60:
            print(f'Автомобиль {self.name} движется с превышением скорости!!!')
        else:
            print(f'Автомобиль {self.name} движется с приемлемой скоростью')


class SportCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)


class WorkCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        print(f'Автомобиль {self.name} движется со скоростью {self.speed} ')
        if self.speed > 40:
            print(f'Автомобиль {self.name} движется с превышением скорости!!!')
        else:
            print(f'Автомобиль {self.name} движется с приемлемой скоростью')


class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def police(self):
        if self.is_police:
            print(f'{self.name} полицейская машина')
        else:
            print(f'{self.name} не автомобиль полиции')


car = Car(70, 'black', 'Jeep', False)
car.go()
mustang = SportCar(100, 'red', 'mustang', False)
six = WorkCar(50, 'white', 'six', False)
volvo = TownCar(40, 'blue', 'volvo', False)
bobik = PoliceCar(70, 'black', 'VAZ', True)
mustang.turn_left()
volvo.show_speed()
bobik.police()
six.show_speed()
