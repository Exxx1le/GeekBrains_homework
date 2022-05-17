# 4. Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад. А также класс «Оргтехника»,
# который будет базовым для классов-наследников. Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс).
# В базовом классе определите параметры, общие для приведённых типов. В классах-наследниках реализуйте параметры,
# уникальные для каждого типа оргтехники.

# 5. Продолжить работу над первым заданием. Разработайте методы, которые отвечают за приём оргтехники на склад и передачу
# в определённое подразделение компании. Для хранения данных о наименовании и количестве единиц оргтехники, а также
# других данных, можно использовать любую подходящую структуру (например, словарь).

# 6. Продолжить работу над вторым заданием. Реализуйте механизм валидации вводимых пользователем данных. Например,
# для указания количества принтеров, отправленных на склад, нельзя использовать строковый тип данных.
# Подсказка: постарайтесь реализовать в проекте «Склад оргтехники» максимум возможностей, изученных на уроках по ООП.

class Stock:
    def __init__(self):
        self.in_stock = {}
        self.in_use = {}

    def __str__(self):
        return f'На складе: {self.in_stock}, \n В подразделении: {self.in_use}'

    def add_printer(self, serial_number, working, print_color):
        Printer(serial_number, working, print_color)
        self.in_stock.setdefault(serial_number, ['принтер', working, print_color])

    def add_scaner(self, serial_number, working, scan_dpi):
        Scaner(serial_number, working, scan_dpi)
        self.in_stock.setdefault(serial_number, ['scaner', working, scan_dpi])

    def add_copier(self, serial_number, working, scan_dpi, print_color):
        Copier(serial_number, working, scan_dpi, print_color)
        self.in_stock.setdefault(serial_number, ['ксерокс', working, scan_dpi, print_color])

    def give_away(self, serial_number):
        try:
            self.in_use.setdefault(serial_number, self.in_stock[serial_number])
            self.in_stock.pop(serial_number)
        except KeyError as e:
            print('Устройства с таким номером нет на складе')

    def return_to_stock(self, serial_number):
        try:
            self.in_stock.setdefault(serial_number, self.in_use[serial_number])
            self.in_use.pop(serial_number)
        except KeyError as e:
            print('Устройства с таким номером нет в подразделении')

    def search_in_stock(self):
        serial_number = input('Введите серийный номер для поиска ')
        try:
            for i in serial_number:
                if i.isdigit() is False:
                    raise SerialNumberError
        except SerialNumberError:
            print('Вы ввели не число')
        else:
            try:
                print(self.in_stock[int(serial_number)])
            except KeyError as e:
                print('Устройства с таким номером нет на складе')


class ОfficeEquipment:
    def __init__(self, serial_number, working):
        self.working = working
        self.serial_number = serial_number


class Printer(ОfficeEquipment):
    def __init__(self, serial_number, working, print_color):
        super().__init__(serial_number, working)
        self.print_color = print_color


class Scaner(ОfficeEquipment):
    def __init__(self, serial_number, working, scan_dpi):
        super().__init__(serial_number, working)
        self.scan_dpi = scan_dpi


class Copier(ОfficeEquipment):
    def __init__(self, serial_number, working, scan_dpi, print_color):
        super().__init__(serial_number, working)
        self.scan_dpi = scan_dpi
        self.print_color = print_color


class SerialNumberError(Exception):
    pass


stock_1 = Stock()
stock_1.add_printer(1231, 'working', 'black and white')
print(stock_1)
stock_1.give_away(1231)
print(stock_1)
stock_1.return_to_stock(1231)
print(stock_1)
stock_1.search_in_stock()
