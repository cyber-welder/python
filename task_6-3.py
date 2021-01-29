"""
Реализовать базовый класс Worker (работник).
    определить атрибуты: name, surname, position (должность), income (доход);
    последний атрибут должен быть защищённым и ссылаться на словарь,
    содержащий элементы: оклад и премия, например, {"wage": wage, "bonus": bonus};
    создать класс Position (должность) на базе класса Worker;
    в классе Position реализовать методы получения полного имени сотрудника (get_full_name)
    и дохода с учётом премии (get_total_income);
    проверить работу примера на реальных данных: создать экземпляры класса Position, передать данные,
    проверить значения атрибутов, вызвать методы экземпляров.
"""


class Worker:
    def __init__(self, name, surname, position, income):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = income


class Position(Worker):
    def get_full_name(self):
        return self.surname + ' ' + self.name

    def get_total_income(self):
        return sum(self._income.values())


person_1 = Position('Иван', 'Иванов', 'Директор', {'Оклад': 100000, 'Премия': 30000})
person_2 = Position('Петр', 'Петров', 'Технический директор', {'Оклад': 85000, 'Премия': 20000})

print('ФИО:', person_1.get_full_name())
print('Должность:', person_1.position)
print('Доход:', person_1.get_total_income())
print()
print('ФИО:', person_2.get_full_name())
print('Должность:', person_2.position)
print('Доход:', person_2.get_total_income())


