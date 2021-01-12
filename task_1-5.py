revenue = float(input('Введите значение прибыли: '))
costs = float(input('Введите значение издержек: '))

if revenue < costs:
    print('Фирма работет в убыток, помочь нечем')
else:
    print('Фирма работет с прибылью')
    print(f'Рентабельность прибыли равна - {(revenue - costs) / revenue * 100:.1f}%')
    count = int(input('Введите количество сотрудников фирмы: '))
    print(f'Чистая прибыль на каждого сотрудника равна - {(revenue - costs) / count:.1f}')
