""" 2. Реализовать проект расчёта суммарного расхода ткани на производство одежды.
Создать абстрактный класс Clothes (одежда). Сделать в этом классе свойство cloth_size
(используя декоратор @property) - размер ткани, необходимый для производства одежды.
Это свойство должно вычислять размерт ткани, вызывая абстрактный метод self.get_size().
Сделать два производных класса одежды: Suit (костюм) и Coat (Пальто).
В конструктор Suit должен принимать параметр height (рост), а Coat - size (размер).
Для определения расхода ткани по каждому типу одежды внутри метода get_size() использовать формулы:

для пальто: (size/6.5 + 0.5)
для костюма: (2*height + 0.3)
Создать список из 10 единиц одежды случайно выбирая один из двух возможных типов со случайным параметром.
Распечатать список одежды: размер требуемой ткани, тип и параметр.
Рассчитать и вывести на экран общий объем ткани, необходимый для пошива всей одежды из этого списка, используя
свойство cloth_size. Например:

30.3 - Suit (height: 15)
20 - Coat (size: 3)
13.5 - Coat (size: 2)
4.3 - Suit (seze: 2)
...
Итого: 250.3"""

from abc import ABC, abstractmethod
import random


class Clothes(ABC):
    @abstractmethod
    def cloth_size(self):
        return self.get_size()

    @abstractmethod
    def get_size(self):
        pass


class Suit(Clothes):
    def __init__(self, height):
        self.__height = height

    @property
    def cloth_size(self):
        return self.get_size()

    def get_size(self):
        return round(2 * self.__height + 0.3, 2)

    def __str__(self):
        return 'Suit (' + str(self.__height) + '): ' + str(self.cloth_size)


class Coat(Clothes):
    def __init__(self, size):
        self.__size = size

    @property
    def cloth_size(self):
        return self.get_size()

    def get_size(self):
        return round(self.__size/6.5 + 0.5, 2)

    def __str__(self):
        return 'Coat (' + str(self.__size) + '): ' + str(self.cloth_size)


sum10 = 0
lst = []
for i in range(10):
    method = random.randint(0, 2)
    num = random.randint(10, 400)
    num /= 10
    if method == 0:
        lst.append(Suit(num))
    else:
        lst.append(Coat(num))
    sum10 += lst[i].cloth_size
    print(lst[i])
print(f'Итого: {sum10:.2f}')
