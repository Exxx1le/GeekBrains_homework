# 5. Реализовать класс Stationery (канцелярская принадлежность).
# определить в нём атрибут title (название) и метод draw (отрисовка). Метод выводит сообщение «Запуск отрисовки»;
# создать три дочерних класса Pen (ручка), Pencil (карандаш), Handle (маркер);
# в каждом классе реализовать переопределение метода draw. Для каждого класса метод должен выводить уникальное сообщение;
# создать экземпляры классов и проверить, что выведет описанный метод для каждого экземпляра.

class Stationery:
    title = 'stationary'

    def draw(self):
        return 'Запуск отрисовки'


class Pen(Stationery):
    def draw(self):
        return 'Запуск отрисовки ручкой'


class Pencil(Stationery):
    def draw(self):
        return 'Запуск отрисовки карандашом'


class Handle(Stationery):
    def draw(self):
        return 'Запуск отрисовки маркером'


stationery_1 = Stationery()
print(stationery_1.draw())

pen_1 = Pen()
print(pen_1.draw())

pencil_1 = Pencil()
print(pencil_1.draw())

handle_1 = Handle()
print(handle_1.draw())
