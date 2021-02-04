"""
Создайте собственный класс-исключение, обрабатывающий ситуацию деления на ноль.
Проверьте его работу на данных, вводимых пользователем.
При вводе нуля в качестве делителя программа должна корректно обработать эту ситуацию и не завершиться с ошибкой.
"""


class OtherError(Exception):
    def __init__(self, txt):
        self.txt = txt


a, b = input('Введите делимое: '), input('Введите делитель: ')

try:
    if int(b) == 0:
        raise OtherError('На ноль делить "низзя"!')
    a = int(a) / int(b)

except ValueError:
    print("Вы ввели не число")

except OtherError as err:
    print(err)

else:
    print(f"Результат: {a:.2f}")
