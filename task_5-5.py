"""
Создать (программно) текстовый файл, записать в него программно набор чисел, разделённых пробелами.
Программа должна подсчитывать сумму чисел в файле и выводить её на экран.
"""
from random import randint

with open('task_5-5.txt', 'w', encoding='UTF-8') as f:
    f.write(' '.join([str(randint(1, 100)) for _ in range(100)]))

with open('task_5-5.txt', 'r', encoding='UTF-8') as f:
    numbers = list(map(int, f.read().split()))

print(sum(numbers))
