"""
3. Пользователь вводит месяц в виде целого числа от 1 до 12.
Сообщить к какому времени года относится месяц (зима, весна, лето, осень).
Напишите решения через list и через dict.
"""

m = int(input('Введите месяц в виде целого числа от 1 до 12: '))

seasons_list = [['зима', 12, 1, 2], ['весна', 3, 4, 5], ['лето', 6, 7, 8], ['осень', 9, 10, 11]]
result = 'Нет такого месяца'
for s in seasons_list:
    if m in s:
        result = 'Это ' + s[0]
print(result)

seasons_dict = {1: 'зима', 2: 'зима', 3: 'весна', 4: 'весна', 5: 'весна', 6: 'лето', 7: 'лето', 8: 'лето', 9: 'осень',
                10: 'осень', 11: 'осень', 12: 'зима'}

print('Это ' + seasons_dict[m] if 0 < m < 13 else 'Нет такого месяца')