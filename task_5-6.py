"""
Сформировать (не программно) текстовый файл.
В нём каждая строка должна описывать учебный предмет и наличие лекционных,
практических и лабораторных занятий по предмету.
Сюда должно входить и количество занятий. Необязательно, чтобы для каждого предмета были все типы занятий.
Сформировать словарь, содержащий название предмета и общее количество занятий по нему. Вывести его на экран.
"""

# регулярки не проходили, но тут прям напрашивается )))
from re import findall

regex = r'(?:[а-яА-ЯёЁ ]+(?=:))|(?:\d+)'

with open('task_5-6.txt', 'r', encoding='UTF-8') as f:
    subjects = f.readlines()

total = {}

for subject in subjects:
    matches = findall(regex, subject)
    key, value = '', []
    for match in matches:
        if match.isnumeric():
            value.append(int(match))
        else:
            key = match
    total[key] = value

# вывод списка
for k, v in total.items():
    print(k, sum(v))
