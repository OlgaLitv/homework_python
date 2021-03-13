"""Задание 5. * Вызов с командной строки
Доработать скрипт из предыдущего задания: теперь он должен работать и из консоли,
а коды валют ему дожны передавать через аргументы командной строки (там может быть один или несколько кодов).
Вывод курсов сделать в том же порядке, что присланные аргументы
Например:
python task5.py USD EUR
USD 75.18, 2020-09-05
EUR 80.35, 2020-09-05"""


def main(argv):
   for code in argv[1:]:
       date_and_currencies = utils.get_currency_rate(code)
       print(code.upper(), str(date_and_currencies[1]) + ', ' + str(date_and_currencies[0]))
   return 0


if __name__ == '__main__':
    import utils
    import sys
    exit(main(sys.argv))
