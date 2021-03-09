"""Задание 3. * Курс Валюты (расширенный)
Доработать функцию get_currency_rate(): теперь она должна возвращать курс и дату,
на которую этот курс действует (взять из того же файла ЦБ РФ).
Для значения курса используйте тип Decimal (https://docs.python.org/3.8/library/decimal.html) вместо float.
Дата должна быть типа datetime.date
"""

from requests import get, utils
import datetime as dt
from decimal import Decimal


def get_currency_rate(currency):
    response = get("http://www.cbr.ru/scripts/XML_daily.asp")
    encodings = utils.get_encoding_from_headers(response.headers)
    content = response.content.decode(encoding=encodings)
    index = content.find('<CharCode>' + currency.upper() + '</CharCode>')
    if index < 0:
        currencies = None
    else:
        index_start = content.find('<Value>', index)
        index_finish = content.find('</Value>', index_start)
        currencies = Decimal(content[index_start+7:index_finish].replace(',', '.'))
    index_date = content.find('Date=')
    text_date = content[index_date + 6:index_date + 16]
    output_date = dt.datetime.strptime(text_date, '%d.%m.%Y').date()
    response.close()
    return output_date, currencies


date_and_currencies = get_currency_rate('USD')
print(f'На дату {date_and_currencies[0]} курс валюты USD к рублю равен', date_and_currencies[1])
date_and_currencies = get_currency_rate('EUR')
print(f'На дату {date_and_currencies[0]} курс валюты EUR к рублю равен', date_and_currencies[1])

input_val = input('Введите код валюты:').upper()
date_and_currencies = get_currency_rate(input_val)
if date_and_currencies[1]:
    print(f'На дату {date_and_currencies[0]} курс валюты {input_val} к рублю равен', date_and_currencies[1])
else:
    print(date_and_currencies[0], date_and_currencies[1])
