"""
Создать программный файл в текстовом формате,
записать в него построчно данные, вводимые пользователем.
Об окончании ввода данных будет свидетельствовать пустая строка.
"""

with open('task_5-1.txt', 'w', encoding='UTF-8') as f:
    while True:
        line = input()
        if not len(line):
            break
        print(line, file=f)
