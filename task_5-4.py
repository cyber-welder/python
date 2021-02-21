"""
Создать (не программно) текстовый файл со следующим содержимым:
One — 1
Two — 2
Three — 3
Four — 4
Напишите программу, открывающую файл на чтение и считывающую построчно данные.
При этом английские числительные должны заменяться на русские.
Новый блок строк должен записываться в новый текстовый файл.
"""

numbers = {'One': 'Один', 'Two': 'Два', 'Three': 'Три', 'Four': 'Четыре'}

with open('task_5-4_eng.txt', 'r', encoding='UTF-8') as f:
    counting = f.read()

for k, v in numbers.items():
    counting = counting.replace(k, v)

with open('task_5-4_rus.txt', 'w', encoding='UTF-8') as f:
    f.write(counting)
