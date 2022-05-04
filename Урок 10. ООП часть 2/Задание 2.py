# 2. Реализовать проект расчёта суммарного расхода ткани на производство одежды. Основная сущность (класс) этого проекта
# — одежда, которая может иметь определённое название. К типам одежды в этом проекте относятся пальто и костюм. У этих
# типов одежды существуют параметры: размер (для пальто) и рост (для костюма). Это могут быть обычные числа: V и H,
# соответственно. Для определения расхода ткани по каждому типу одежды использовать формулы: для пальто (V/6.5 + 0.5),
# для костюма(2*H + 0.3). Проверить работу этих методов на реальных данных. Выполнить общий подсчёт расхода ткани.
# Проверить на практике полученные на этом уроке знания. Реализовать абстрактные классы для основных классов проекта
# и проверить работу декоратора @property.

from abc import ABC, abstractmethod


class Clothes(ABC):
    count = 0

    @abstractmethod
    def expence(self):
        pass


class Coat(Clothes):
    def __init__(self, size):
        self.size = size
        Coat.count += self.expence

    def __str__(self):
        return f'Размер {self.size}, расход {self.expence:.02f}, общий расход {Coat.count:.02f}'

    @property
    def expence(self):
        exp = self.size / 6.5 + 0.5
        return float(exp)


class Suit(Clothes):
    def __init__(self, height):
        self.height = height
        Suit.count += self.expence

    def __str__(self):
        return f'Рост {self.height}, расход {self.expence:.02f}, общий расход {Suit.count:.02f}'

    @property
    def expence(self):
        exp = (self.height * 2 + 0.3) / 100
        return float(exp)


cloth_1 = Coat(30)
print(cloth_1)
cloth_2 = Suit(25)
print(cloth_2)
