"""4. Реализовать класс Stationery (канцелярская принадлежность).
определить в нём атрибут title (название) и метод draw() (отрисовка). Метод выводит сообщение «Запуск отрисовки»;
создать три производных класса Pen (ручка), Pencil (карандаш), Handle (маркер);
в каждом классе переопределить метод draw(). Для каждого класса метод должен выводить уникальное сообщение;
создать экземпляры каждого класса и положить их в список. Проитерироваться по этому списку и вызвать метод draw() для
каждого элемента."""


class Stationery:

    def __init__(self, title):
        self.__title = title

    def get_title(self):
        return self.__title

    def draw(self):
        print('запуск отрисовки')


class Pen(Stationery):

    def draw(self):
        print('рисует', super().get_title())


class Pencil(Stationery):

    def draw(self):
        print('рисует', super().get_title())


class Handle(Stationery):

    def draw(self):
        print('рисует', super().get_title())


st = Stationery('канцелярская принадлежность')
pen1 = Pen('ручка Erich Crauser')
pen2 = Pen('ручка Stabilo')
handle1 = Handle('маркер Stabilo')
pencil1 = Pencil('карандаш Koohinoor')
lst = [st, pen1, pen2, pencil1, handle1]
for x in lst:
    x.draw()
