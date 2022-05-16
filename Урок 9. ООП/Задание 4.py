# 4. Реализуйте базовый класс Car.
# у класса должны быть следующие атрибуты: speed, color, name, is_police(булево). А также методы:
# go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась, повернула (куда);
# опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar;
# добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля;
# для классов TownCar и WorkCar переопределите метод show_speed.
# При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.

class Car:
    def __init__(self, speed, color, name, is_police=False):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        return 'Машина поехала'

    def stop(self):
        return 'Машина остановилась'

    def turn(self, where):
        if where == 'left':
            return 'Машина повернула налево'
        elif where == 'right':
            return 'Машина повернула направо'

    def show_speed(self):
        return self.speed


class TownCar(Car):
    def show_speed(self):
        if self.speed > 60:
            return 'Превышение скорости'
        else:
            return self.speed


class SportCar(Car):
    pass


class WorkCar(Car):
    def show_speed(self):
        if self.speed > 40:
            return 'Превышение скорости'
        else:
            return self.speed


class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police=True):
        super().__init__(speed, color, name, is_police)


town_car_1 = TownCar(70, 'black', 'audi')
print(town_car_1.show_speed())

work_car_1 = WorkCar(41, 'yellow', 'cat')
print(work_car_1.show_speed())

police_car_1 = PoliceCar(50, 'white', 'ford')
print(police_car_1.is_police)
