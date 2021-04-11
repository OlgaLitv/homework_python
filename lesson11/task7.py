"""7. Реализовать проект «Операции с комплексными числами». Создайте класс «Комплексное число». Реализуйте
перегрузку методов сложения и умножения комплексных чисел. Проверьте работу проекта. Для этого создаёте экземпляры
класса (комплексные числа), выполните сложение и умножение созданных экземпляров. Проверьте корректность полученного
результата."""


class ComplexNumber:
    def __init__(self, imaginary=0, real_part=0):
        if (isinstance(imaginary, float) or isinstance(imaginary, int)) \
                and (isinstance(real_part, int) or isinstance(real_part, float)):
            self.__real, self.__imaginary = real_part, imaginary
        else:
            raise ValueError('Возможны только типы int и float для создания комплексного числа!')

    def __add__(self, other):
        if isinstance(other, ComplexNumber):
            return ComplexNumber(self.__imaginary + other.__imaginary, self.__real + other.__real)
        elif isinstance(other, int) or isinstance(other, float):
            return ComplexNumber(self.__imaginary, self.__real + other)
        else:
            raise ValueError('складывать можно только числа!')

    def __mul__(self, other):
        if isinstance(other, ComplexNumber):
            return ComplexNumber(self.__imaginary * other.__real + self.__real * other.__imaginary,
                                 self.__real * other.__real - self.__imaginary * other.__imaginary)
        elif isinstance(other, int) or isinstance(other, float):
            return ComplexNumber(self.__imaginary * other, self.__real * other)
        else:
            raise ValueError('умножать можно только числа!')

    def __str__(self):
        real_part = '' if self.__real == 0 else '+' + str(self.__real) if self.__real > 0 else str(self.__real)
        imaginary = 'i' if self.__imaginary == 1 else '-i' if self.__imaginary == -1 else '0' \
            if self.__imaginary == 0 and real_part == '' else '' if self.__imaginary == 0 else f'{self.__imaginary}i'
        return imaginary + real_part


c1 = ComplexNumber(1.4)
c2 = ComplexNumber(14, -3)
c3 = ComplexNumber(-2.9, 3)
print(f'c1 = {c1}     c2 = {c2}     c3 = {c3}')
print(f'c1 + c2 = {c1+c2}         c2 + 30.5 = {c2+30.5}')
print(f'c2 * c3 = {c2*c3}      c2 * 0 = {c2*0}')
try:
    print(f'c2 * "0" ={c2 * "0"}')
except ValueError as err:
    print(err)
try:
    c4 = ComplexNumber(1, 'two')
    print(f'c4 ={c4}')
except ValueError as err:
    print(err)
