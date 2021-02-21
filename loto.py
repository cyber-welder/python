"""
== Лото ==

Правила игры в лото.

Игра ведется с помощью спе циальных карточек, на которых отмечены числа,
и фишек (бочонков) с цифрами.

Количество бочонков — 90 штук (с цифрами от 1 до 90).

Каждая карточка содержит 3 строки по 9 клеток. В каждой строке по 5 случайных цифр,
расположенных по возрастанию. Все цифры в карточке уникальны. Пример карточки:

--------------------------
    9 43 62          74 90
 2    27    75 78    82
   41 56 63     76      86
--------------------------

В игре 2 игрока: пользователь и компьютер. Каждому в начале выдается
случайная карточка.

Каждый ход выбирается один случайный бочонок и выводится на экран.
Также выводятся карточка игрока и карточка компьютера.

Пользователю предлагается зачеркнуть цифру на карточке или продолжить.
Если игрок выбрал "зачеркнуть":
    Если цифра есть на карточке - она зачеркивается и игра продолжается.
    Если цифры на карточке нет - игрок проигрывает и игра завершается.
Если игрок выбрал "продолжить":
    Если цифра есть на карточке - игрок проигрывает и игра завершается.
    Если цифры на карточке нет - игра продолжается.

Побеждает тот, кто первый закроет все числа на своей карточке.

Пример одного хода:

Новый бочонок: 70 (осталось 76)
------ Ваша карточка -----
 6  7          49    57 58
   14 26     -    78    85
23 33    38    48    71
--------------------------
-- Карточка компьютера ---
 7 87     - 14    11
      16 49    55 88    77
   15 20     -       76  -
--------------------------
Зачеркнуть цифру? (y/n)

Подсказка: каждый следующий случайный бочонок из мешка удобно получать
с помощью функции-генератора.

Подсказка: для работы с псевдослучайными числами удобно использовать
модуль random: http://docs.python.org/3/library/random.html

"""

from random import shuffle, sample, randint


class Gamer:
    """ Игрок. Принимает имя игрока. Методом pull_card получает карточку (Card) """
    def __init__(self, name):
        """
        :param name: имя игрока
        """
        self.name = name
        self.gamer_card = []    # карточка игрока
        self.answer = ''    # ответ
        self.true_answer = True  # правильность ответа
        self.end_card = False   # заполненость карточки

    def pull_card(self, gamer_card):
        """
        Присваивает карточку игроку
        :param gamer_card: карточка игрока
        """
        self.gamer_card = gamer_card


class Card:
    """ Карточка лото. Генерируется при создании"""
    def __init__(self):
        self.cells, cells = [], []
        nums = [['1', '2', '3', '4', '5', '6', '7', '8', '9'],
                ['10', '11', '12', '13', '14', '15', '16', '17', '18', '19'],
                ['20', '21', '22', '23', '24', '25', '26', '27', '28', '29'],
                ['30', '31', '32', '33', '34', '35', '36', '37', '38', '39'],
                ['40', '41', '42', '43', '44', '45', '46', '47', '48', '49'],
                ['50', '51', '52', '53', '54', '55', '56', '57', '58', '59'],
                ['60', '61', '62', '63', '64', '65', '66', '67', '68', '69'],
                ['70', '71', '72', '73', '74', '75', '76', '77', '78', '79'],
                ['80', '81', '82', '83', '84', '85', '86', '87', '88', '89', '90']]
        # далее весьма мутный код формирования карточки по правилам лото
        unique_nums = [sample(dec, 3) for dec in nums]  # уникальные значения не более трех в каждом десятке
        for i in range(3):
            cells.append([n[i] for n in unique_nums])
            empty = sample(cells[i], 4)
            for c in empty:
                cells[i][cells[i].index(c)] = ' '
            self.cells.extend(cells[i])

    def __str__(self):
        return '\n'.join(['\t'.join(list(map(str, self.cells[9 * i:9 * i + 9]))) for i in range(3)])


class Bag:
    """ Мешок с бочонками (1-90). Метод pull_barrel вытаскивает бочонки по одному пока они не кончатся """
    def __init__(self):
        self.barrels = list(map(str, range(1, 91)))
        shuffle(self.barrels)

    def pull_barrel(self):
        """
        Метод "достает" бочонок
        :return: возвращает номер изъятого бочонка
        """
        if len(self.barrels):
            return self.barrels.pop()


class Game:
    """ Игра """
    def __init__(self, diff, bag, *gamers):
        """
        :param diff: сложность 0-3
        :param bag: список с бочонками (Bag)
        :param gamers: игроки (Gamer)
        """
        self.gamers = gamers
        self.bag = bag
        self.diff = 3 - int(diff)

    @staticmethod
    def _available(gamer, barrel):
        return barrel in gamer.gamer_card.cells

    def _end_card(self):
        """
         Проверяет заполнение карточек игроков.
        :return: строка с победителями или пустая если их нет
        """
        result, draw = '', 0
        for gamer in self.gamers:
            gamer.end_card = True
            for i in gamer.gamer_card.cells:
                if i.isdigit():
                    gamer.end_card = False
            draw += gamer.end_card
            if gamer.end_card:
                result += f'Победил игрок {gamer.name}'.center(len(gamer.name) + 17, ' ').center(34, '-') + '\n'

        if len(result):
            if draw > 1:
                result += '!!!Ничья!!!'.center(34, '=')
            return result
        else:
            return ''

    def _check_answer(self, barrel):
        """
        Проверяет правильность ответов
        :param barrel: номер бочонка
        :return: строка с проигравшими или пустая, если их нет
        """
        result, draw = '', 0
        for gamer in self.gamers:
            if self._available(gamer, barrel):
                gamer.gamer_card.cells[gamer.gamer_card.cells.index(barrel)] = '-'
                gamer.true_answer = True if gamer.answer.lower() == 'y' else False
            else:
                gamer.true_answer = False if gamer.answer.lower() == 'y' else True
            draw += gamer.true_answer
            if not gamer.true_answer:
                result += f'{gamer.name} дал не верный ответ'.center(len(gamer.name) + 22, ' ').center(34, '-') + '\n'

        if len(result):
            if not draw:
                result += '!!!Ничья!!!'.center(34, '=')
            return result
        else:
            return ''

    def start(self):
        while True:
            chance = randint(1, 100)
            barrel = bag.pull_barrel()
            print('Бочонок с номером:', barrel, 'Осталось:', len(self.bag.barrels))
            for gamer in self.gamers:
                print(gamer.name.center((len(gamer.name) + 2), ' ').center(34, '-'))
                print(gamer.gamer_card)
                print('-' * 34)
            self.gamers[0].answer = input('Зачеркнуть цифру? (y/n): ')
            self.gamers[1].answer = 'y' if self._available(self.gamers[1], barrel) else 'n'
            if chance < self.diff * 5:
                self.gamers[1].answer = 'y' if self.gamers[1].answer == 'n' else 'n'
            print()
            print('=' * 34)
            # Проверка правильности ответов
            result = self._check_answer(barrel)
            if len(result):
                break
            # Проверка заполнения карточки
            result = self._end_card()
            if len(result):
                break
        print(result)


bag = Bag()

gamer1 = Gamer(input('Введите свое имя: '))
gamer2 = Gamer('Compukter')

gamer1.pull_card(Card())
gamer2.pull_card(Card())

game = Game(input('Введите сложность игры числом от 3 (сложно) до 0 (легко): '), bag, gamer1, gamer2)

game.start()
