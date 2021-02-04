"""
Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки формата «день-месяц-год».
В рамках класса реализовать два метода. Первый, с декоратором @classmethod.
Он должен извлекать число, месяц, год и преобразовывать их тип к типу «Число».
Второй, с декоратором @staticmethod, должен проводить валидацию числа, месяца и года (например, месяц — от 1 до 12).
Проверить работу полученной структуры на реальных данных.
"""

from datetime import date

class StrDate:
    def __init__(self, dt):
        self._date = dt

    @property
    def date(self):
        return StrDate.srt_to_int(self._date)

    @classmethod
    def srt_to_int(cls, dt):
        try:
            return list(map(int, dt.split('-')))
        except ValueError:
            print('Не верный формат даты "ДД-ММ-ГГГГ"')

    @staticmethod
    def correct(dt):
        try:
            d = date(dt[2], dt[1], dt[0])
            return True
        except ValueError:
            return False


d = StrDate('12-02-2021')

if d.correct(d.date):
    print(*d.date)
