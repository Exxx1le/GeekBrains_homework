# 7. Реализовать проект «Операции с комплексными числами». Создайте класс «Комплексное число».
# Реализуйте перегрузку методов сложения и умножения комплексных чисел.
# Проверьте работу проекта. Для этого создаёте экземпляры класса (комплексные числа),
# выполните сложение и умножение созданных экземпляров. Проверьте корректность полученного результата.

class ComplexNumbers:
    def __init__(self, real, imag=0):
        self.__complex = complex(real, imag)

    def __add__(self, other):
        if isinstance(other, ComplexNumbers):
            other = other.__complex

        complex_ = self.__complex + other
        return ComplexNumbers(complex_.real, int(complex_.imag))

    def __mul__(self, other):
        if isinstance(other, ComplexNumbers):
            other = other.__complex

        complex_ = self.__complex * other
        return ComplexNumbers(complex_.real, int(complex_.imag))

    def __str__(self):
        return self.__complex.__str__()


number_1 = ComplexNumbers(3, 6)
number_2 = ComplexNumbers(4)
print(number_1 + number_2, complex(2, -3) + complex(5))
print(number_1 * number_2, complex(2, -3) + complex(5))
