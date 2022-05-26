# 1. Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде
# строки формата «день-месяц-год». В рамках класса реализовать два метода. Первый — с
# декоратором @classmethod. Он должен извлекать число, месяц, год и преобразовывать их тип
# к типу «Число». Второй — с декоратором @staticmethod, должен проводить валидацию числа,
# месяца и года (например, месяц — от 1 до 12). Проверить работу полученной структуры на
# реальных данных.

class Date:
    date = None

    def __init__(self, date_string):
        self.date_string = date_string
        Date.date = self.date_string

    def __str__(self):
        return str(self.date_string)

    @classmethod
    def date_to_int(cls):
        int_list = [int(i) for i in cls.date.split('-')]
        return int_list

    @staticmethod
    def date_check(date):
        int_list = [int(i) for i in date.split('-')]
        if int_list[0] > 31:
            raise ValueError('Wrong date')
        elif int_list[1] > 12:
            raise ValueError('Wrong month')
        else:
            return 'Date is ok!'


date_1 = Date('17-12-88')
print(Date.date)
print(Date.date_to_int())
print(Date.date_check('17-12-88'))
