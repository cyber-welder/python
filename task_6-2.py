"""
Реализовать класс Road (дорога).
    определить атрибуты: length (длина), width (ширина);
    значения атрибутов должны передаваться при создании экземпляра класса;
    атрибуты сделать защищёнными;
    определить метод расчёта массы асфальта, необходимого для покрытия всей дороги;
    использовать формулу: длина * ширина * масса асфальта для покрытия одного кв. метра дороги асфальтом,
    толщиной в 1 см * число см толщины полотна;
    проверить работу метода.
Например: 20м * 5000м * 25кг * 5см = 12500 т.
"""


class Road:
    def __init__(self, length, width):
        self._width = width
        self._length = length

    def get_weight(self):
        return self._length * self._width * 25 * 5


r = Road(10, 1000)
print(r.get_weight()/1000, 'тонн')
