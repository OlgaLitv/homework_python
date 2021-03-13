"""Задание 2. Курс Валюты
Написать функцию get_currency_rate(), принимающую в качестве аргумента код валюты
(например, USD, EUR, GBP, ...) в виде строки и возвращающую курс этой валюты по отношению к рублю.
Код валюты может быть в произвольном регистре.
Функция должна возвращать результат числового типа, например float.
Если в качестве аргумента передали код валюты, которого нет в ответе, вернуть None.
Используйте библиотеку requests, чтобы забрать актуальные данные из ЦБ РФ по адресу
http://www.cbr.ru/scripts/XML_daily.asp.

Выведите на экран курсы для доллара и евро, используя написанную функцию."""


from requests import get, utils


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
        currencies = float(content[index_start+7:index_finish].replace(',', '.'))
    response.close()
    return currencies


currencies_value = get_currency_rate('USD')
print(f'Курс валюты USD к рублю равен', currencies_value)
currencies_value = get_currency_rate('EUR')
print(f'Курс валюты EUR к рублю равен', currencies_value)

input_val = input('Введите код валюты:').upper()
currencies_value = get_currency_rate(input_val)
if currencies_value:
    print(f'Курс валюты {input_val} к рублю равен', currencies_value)
else:
    print(currencies_value)
