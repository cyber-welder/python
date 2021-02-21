"""
Реализуйте базовый класс Car.
    у класса должны быть следующие атрибуты: speed, color, name, is_police (булево).
    А также методы: go, stop, turn(direction), которые должны сообщать,
    что машина поехала, остановилась, повернула (куда);
    опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar;
    добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля;
    для классов TownCar и WorkCar переопределите метод show_speed.
    При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
Создайте экземпляры классов, передайте значения атрибутов.
Выполните доступ к атрибутам, выведите результат. Вызовите методы и покажите результат.
"""


class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def show_speed(self):
        print('Скорость', self.speed, 'км')

    def go(self):
        print('Машина поехала')

    def stop(self):
        print('Машина остановилась')

    def turn(self, turned):
        print('Машина повернула', turned)


class TownCar(Car):
    def show_speed(self):
        print('Скорость', self.speed, 'км', '- Скорость превышена!' if self.speed > 60 else '')


class SportCar(Car):
    pass


class WorkCar(Car):
    def show_speed(self):
        print('Скорость', self.speed, 'км', '- Скорость превышена!' if self.speed > 40 else '')


class PoliceCar(Car):
    pass


car1 = TownCar(35, 'Серая', 'Toyota', False)
car2 = SportCar(110, 'Красная', 'Honda', False)
car3 = WorkCar(35, 'Черная', 'Reno', False)
car4 = PoliceCar(60, 'Синяя', 'Калина', True)

cars = [car1, car2, car3, car4]

for car in cars:
    print('----------------------')
    print(car.color, car.name)
    car.go()
    car.show_speed()
    car.turn('вправо')
    car.turn('влево')
    car.speed = 65
    car.show_speed()
    car.stop()
    print('Это полиция -', car.is_police)
