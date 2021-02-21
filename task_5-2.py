"""
Создать текстовый файл (не программно), сохранить в нём несколько строк,
выполнить подсчёт строк и слов в каждой строке.
"""

with open('task_5-2.txt', 'r', encoding='UTF-8') as f:
    file = f.readlines()

[print(f'Слов в стоке {i}: {len(string.split())}') for i, string in enumerate(file)]

print('Всего строк', len(file))
