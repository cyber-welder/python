"""
Реализовать проект расчета суммарного расхода ткани на производство одежды.
Основная сущность (класс) этого проекта — одежда, которая может иметь определенное название.
К типам одежды в этом проекте относятся пальто и костюм.
У этих типов одежды существуют параметры:
    размер (для пальто) и рост (для костюма).
Это могут быть обычные числа: V и H, соответственно.
Для определения расхода ткани по каждому типу одежды использовать формулы:
    для пальто (V/6.5 + 0.5),
    для костюма (2*H + 0.3).
Проверить работу этих методов на реальных данных.
Реализовать общий подсчет расхода ткани.
Проверить на практике полученные на этом уроке знания: реализовать абстрактные классы для основных классов проекта,
проверить на практике работу декоратора @property.
"""

from abc import ABC, abstractmethod


class Clothes(ABC):
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def get_expense(self):
        pass


# пальто
class Coat(Clothes):
    def __init__(self, name, size):
        super().__init__(name)
        self._size = size

    @property
    def size(self):
        # ограничение ввода размеров 40 - 62
        self._size = 40 if self._size < 40 else 62 if self._size > 62 else self._size
        return self._size

    def get_expense(self):
        return self.size / 6.5 + 0.5


# костюм
class Suit(Clothes):
    def __init__(self, name, height):
        super().__init__(name)
        self._height = height

    @property
    def height(self):
        # ограничение ввода роста 1.1 - 2.3
        self._height = 1.1 if self._height < 1.1 else 2.3 if self._height > 2.3 else self._height
        return self._height

    def get_expense(self):
        return 2 * self.height + 0.3


coat = Coat('Пальто', 52)
suit = Suit('Костюм', 1.8)

print(f'Расход ткани для {coat.name} - {coat.get_expense():.1f}')
print(f'Расход ткани для {suit.name} - {suit.get_expense():.1f}')
