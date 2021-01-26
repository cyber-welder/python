"""
Создать текстовый файл (не программно).
Построчно записать фамилии сотрудников и величину их окладов (не менее 10 строк).
Определить, кто из сотрудников имеет оклад менее 20 тысяч, вывести фамилии этих сотрудников.
Выполнить подсчёт средней величины дохода сотрудников
"""

with open('task_5-3.txt', 'r', encoding='UTF-8') as f:
    salaries = {line.split()[0]: float(line.split()[1]) for line in f}

print('Оклад менее 20 тысяч имеют:')
print(*['\t' + name for name, salary in salaries.items() if salary < 20000], sep='\n')

print('Средняя величина дохода:', sum(salaries.values()) / len(salaries))
