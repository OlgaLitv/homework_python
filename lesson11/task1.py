"""1. Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки формата
«день-месяц-год». В рамках класса реализовать два метода. Первый, с декоратором @classmethod. Он должен извлекать
число, месяц, год и преобразовывать их тип к типу «Число». Второй, с декоратором @staticmethod, должен проводить
валидацию числа, месяца и года (например, месяц — от 1 до 12). Проверить работу полученной структуры на реальных
данных."""

import random


class MyData:
    def __init__(self, data_str):
        self._data_str = data_str
        self._day, self._month, self._year = data_str.split('-')

    @classmethod
    def convert_to_num(cls, data_str):
        try:
            d2, m2, y2 = data_str.split('-')
            return int(d2), int(m2), int(y2)
        except ValueError:
            print('введите дату в правильном формате')

    @staticmethod
    def check_date(date_int_tuple):
        d3, m3, y3 = date_int_tuple[0], date_int_tuple[1], date_int_tuple[2]
        lst31 = [1, 3, 5, 7, 8, 10, 12]  # в этих месяцах по 31 дню
        lst30 = [4, 6, 9, 11]  # в этих месяцах по 30 дней
        if m3 > 12 or m3 < 0:
            print('Неверное значение месяца ' + str(m3) + ' в дате ' + f'{d3:02d}-{m3:02d}-{y3:04d}')
            return False
        if m3 in lst30 and d3 > 30 or m3 in lst31 and d3 > 31 or d3 < 0:
            print('Неверное количество дней ' + str(d3) + ' в дате ' + f'{d3:02d}-{m3:02d}-{y3:04d}')
            return False
        if m3 == 2:
            leap_year = y3 % 4 == 0 and (y3 % 100 != 0 or y3 % 400 == 0)  # признак високосного года
            if leap_year and d3 > 29 or not leap_year and d3 > 28:
                print('Неверное количество дней в феврале: ' + str(d3) + ' в дате ' + f'{d3:02d}-{m3:02d}-{y3:04d}')
                return False
        return True


dates_lst = []
for _ in range(50):
    d1, m1, y1 = random.randint(0, 33), random.randint(0, 13), random.randint(1900, 2101)
    str_date = f'{d1:02d}-{m1:02d}-{y1:04d}'
    print(str_date, MyData.check_date(MyData.convert_to_num(str_date)))

print('29-02-2000', MyData.check_date(MyData.convert_to_num('29-02-2000')))
print('29-02-2001', MyData.check_date(MyData.convert_to_num('29-02-2001')))
