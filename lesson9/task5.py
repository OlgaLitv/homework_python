"""5. Реализуйте базовый класс Car.
при создании класса должны быть переданы атрибуты: color (str), name (str).
реализовать в классе методы: go(speed), stop(), turn(direction), которые должны изменять состояние машины -
для хранения этих свойств вам понадобятся дополнительные атрибуты - придумайте какие.
добавьте метод is_police() - который возвращает True/False, в зависимости от того является ли этот автомобиль
полицейским (см.дальше)
Сделайте несколько производных классов: TownCar, SportCar, WorkCar, PoliceCar;
Добавьте в базовый класс метод get_status(), который должен возвращать в виде строки название, цвет, текущую
скорость автомобиля и направление движения (в случае если автомобиль едет), для полицейских автомобилей перед
названием автомобиля должно идти слово POLICE;
Для классов TownCar и WorkCar в методе get_status() рядом со значением скорости должна выводиться фраза
"ПРЕВЫШЕНИЕ!", если скорость превышает 60 (TownCar) и 40 (WorkCar).
Создайте по одному экземпляру каждого производного класса. В цикле из 10 итераций, для каждого автомобиля
сделайте одно из случайных действий: go, stop, turn со случайными параметрами. После каждого действия
показывайте статус автомобиля."""

import random


class Car:

    def __init__(self, name, color, police=False, max_speed=180):
        self._name = name
        self._color = color
        self._MAX_SPEED = max_speed
        self._current_speed = 0
        self._is_police = police
        self._direction = 'straight'

    def go(self, speed=10):
        self._current_speed = speed if speed <= self._MAX_SPEED else self._MAX_SPEED

    def stop(self):
        self._current_speed = 0

    def turn(self, direction='left'):
        self._direction = direction

    def is_police(self):
        return self._is_police

    def get_status(self):
        answer = self._name + ' ' + self._color
        answer += ' ' + self._direction if self._current_speed != 0 else ''
        return answer + ' ' + str(self._current_speed)


class TownCar(Car):

    def __init__(self, name, color, max_speed=160):
        super(TownCar, self).__init__(name, color, max_speed=max_speed)

    def get_status(self):
        answer = super().get_status()
        answer += ' ПРЕВЫШЕНИЕ ' if self._current_speed > 60 else ''
        return answer


class SportCar(Car):

    def __init__(self, name, color, max_speed=250):
        super().__init__(name, color, max_speed=max_speed)


class WorkCar(Car):

    def __init__(self, name, color, max_speed=100):
        super().__init__(name, color, max_speed=max_speed)

    def get_status(self):
        answer = super().get_status()
        answer += ' ПРЕВЫШЕНИЕ ' if self._current_speed > 40 else ''
        return answer


class PoliceCar(Car):

    def __init__(self, name, color, max_speed=160):
        super().__init__(name, color, max_speed=max_speed, police=True)

    def get_status(self):
        return 'POLICE ' + super().get_status()


car1 = TownCar('VOLVO', 'green')
car2 = SportCar('SUBARU', 'white')
car3 = WorkCar('RENO', 'black')
car4 = PoliceCar('FORD', 'red')
car_lst = [car1, car2, car3, car4]
directions = ('straight', 'left', 'right', 'back')
actions = (Car.go, Car.stop, Car.turn)
for i in range(10):
    num = random.randint(0, 2)
    print('action:', actions[num].__name__)
    for car in car_lst:
        if num == 0:
            idx_speed = random.randint(1, 9)
            actions[num](car, speed=idx_speed * 10)
        elif num == 1:
            actions[num](car)
        else:
            idx_dir = random.randint(0, 3)
            actions[num](car, directions[idx_dir])

        print(car.get_status())
    print('----------------------------------')
