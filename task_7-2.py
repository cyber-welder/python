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

class Clothes:
    def __init__(self, name):
        self.name = name

# пальто
class Coat(Clothes):
    def __init__(self, name, size):
        super().__init__(name)
        self._size = 40
        self.size = size

    @property
    def size(self):
        return self._size

    @size.setter
    # ограничение ввода размеров 40 - 62
    def size(self, size):
        self._size = 40 if size < 40 else 62 if size > 62 else size


    def get_expense(self):
        return self.size / 6.5 + 0.5

# костюм
class Suit(Clothes):
    def __init__(self, name, height):
        super().__init__(name)
        self.height = height

    def get_expense(self):
        return 2 * self.height + 0.3

coat = Coat('Пальто', 52)
suit = Suit('Костюм', 1.8)

print(f'Расход ткани для {coat.name} - {coat.get_expense():.1f}')
print(f'Расход ткани для {suit.name} - {suit.get_expense():.1f}')


