# Создать собственный класс-исключение, обрабатывающий ситуацию деления на ноль.
# Проверить его работу на данных, вводимых пользователем. При вводе нуля в качестве
# делителя программа должна корректно обработать эту ситуацию и не завершиться с ошибкой.

class ZeroError(Exception):
    def __init__(self, txt):
        self.txt = txt


inp_number1 = int(input('Введите число 1 для деления '))
inp_number2 = int(input('Введите число 2 в качестве делителя '))

try:
    int_number = int(inp_number2)
    if inp_number2 == 0:
        raise ZeroError("Вы ввели 0 в качестве делителя!")
except ZeroError as e:
    print(e)
else:
    print(f"Резльутат деления: {int(inp_number1 / inp_number2)}")
