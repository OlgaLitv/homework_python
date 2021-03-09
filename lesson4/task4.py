"""Задание 4. Модуль utils
Написать свой модуль utils и перенести в него функцию get_currency_rate() из предыдущего задания (второго или третьего).
Создать скрипт (task4.py), в котором импортировать этот модуль и выполнить вызовы
функции get_currency_rate() для доллара и евро. Результат вывести на экран в виде:

если используется функция из 2-го задания:
USD 75.18
EUR 80.35
либо, если используется функция из 3-го задания
USD 75.18, 2020-09-05
EUR 80.35, 2020-09-05"""


import utils


date_and_currencies = utils.get_currency_rate('USD')
print('USD', str(date_and_currencies[1]) + ', ' + str(date_and_currencies[0]))
date_and_currencies = utils.get_currency_rate('EUR')
print('EUR', str(date_and_currencies[1]) + ', ' + str(date_and_currencies[0]))
