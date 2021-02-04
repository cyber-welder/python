"""
Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад.
А также класс «Оргтехника», который будет базовым для классов-наследников.
Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс).
В базовом классе определите параметры, общие для приведённых типов.
В классах-наследниках реализуйте параметры, уникальные для каждого типа оргтехники.
"""


class Storage:
    def __init__(self):
        pass


class Equipment:
    def __init__(self, model, list_format, speed, price):
        self.model = model
        self.list_format = list_format
        self.speed = speed
        self.price = price


class Printer(Equipment):
    def __init__(self, model, list_format, price, speed, print_type, print_color=False):
        super().__init__(model, list_format, speed, price)
        self.print_color = print_color
        self.print_type = print_type


class Scaner(Equipment):
    def __init__(self, model, list_format, price, speed, scan_type):
        super().__init__(model, list_format, speed, price)
        self.scan_type = scan_type


class Xerox(Equipment):
    def __init__(self, model, list_format, price, speed, copy_color=False):
        super().__init__(model, list_format, speed, price)
        self.copy_color = copy_color


p1 = Printer('Canon LBP6600', 'A4', 5000, 20, 'Лазерный')
p2 = Printer('HP Officejet 202' 'A4', 17200, 10, 'Струйный', True)
p3 = Printer('Xerox Phaser 6510N', 'A4', 30000, 28, 'Лазерный', True)
p4 = Printer('Brother HL-L2340DWR', 'A4', 11700, 26, 'Лазерный')
p5 = Printer('Epson L132', 'A4', 12000, 28, 'Струйный', True)

s1 = Scaner('Canon CanoScan LiDE 300', 'A4', 5200, 6, 'Планшетный')
s2 = Scaner('Espada E-IScan', 'A4', 4200, 1, 'Ручной')
s3 = Scaner('Epson Perfection V19', 'A4', 6800, 6, 'Планшетный')
s4 = Scaner('Brother DS-640', 'A4', 10000, 15, 'Протяжной')
s5 = Scaner('Kodak ScanMate i940', 'A4', 15300, 20, 'Протяжной')

c1 = Xerox('Xerox WorkCentre 3025V_BI', 'A4', 13000, 20, True)
c2 = Xerox('Brother DCP-L2500DR', 'A4', 16500, 26, True)
c3 = Xerox('HP LaserJet Pro MFP M28', 'A4', 12000, 12)
c4 = Xerox('Pantum M6500', 'A4', 10200, 22, True)
c5 = Xerox('Canon i-SENSYS MF237', 'A4', 31000, 23)


print()

