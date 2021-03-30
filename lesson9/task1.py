"""1. Создать класс TrafficLight (светофор).
определить у него один приватный атрибут color (цвет) и метод get_current_signal() (получить текущий цвет);
после создания экземпляра светофора, он запускает режим смены сигналов с разной длительностью: красный (3 сек),
жёлтый (1 сек), зелёный (3 сек);
переключение идет циклично в порядке красный-жетлый-зеленый-красный-жетлый-зеленый-красный-...
проверить переключение режимов работы светофора, опрашивая в цикле текущее состояние светофора с интервалом 0.5 секунды,
используя метод get_current_signal()
"""

import time
import datetime


class TrafficLight:

    def __init__(self):
        self.__color = 'red'
        self.__start_time = datetime.datetime.now()

    def get_current_signal(self):
        """ находим остаток от деления на 7, так как один цикл (красный-желтый-зеленый) занимает 7 секунд"""
        delta = (datetime.datetime.now() - self.__start_time).total_seconds() % 7
        if delta >= 4:
            self.__color = 'green'
        elif delta >= 3:
            self.__color = 'yellow'
        else:
            self.__color = 'red'
        return self.__color


traffic_l = TrafficLight()
for i in range(42):
    print(i, traffic_l.get_current_signal())
    time.sleep(0.5)
