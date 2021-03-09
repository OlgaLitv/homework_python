from requests import get, utils
import datetime as dt
import xml.etree.ElementTree as ET
from decimal import Decimal


def get_currency_rate(currency):
    response = get("http://www.cbr.ru/scripts/XML_daily.asp")
    encodings = utils.get_encoding_from_headers(response.headers)
    content = response.content.decode(encoding=encodings)
    response.close()
    tree = ET.ElementTree(ET.fromstring(content))
    root = tree.getroot()
    text_date = root.attrib['Date']
    output_date = dt.datetime.strptime(text_date, '%d.%m.%Y').date()
    for child in root:
        find_char_code = False
        for child2 in child:
            if child2.tag == 'CharCode' and child2.text == currency.upper():
                find_char_code = True
            if find_char_code and child2.tag == 'Value':
                return output_date, round(Decimal(child2.text.replace(',', '.')), 2)
    return output_date, None


if __name__ == '__main__':
    date_and_currencies = get_currency_rate('CAD')
    print('CAD', str(date_and_currencies[1]) + ', ' + str(date_and_currencies[0]))
    date_and_currencies = get_currency_rate('UAH')
    print('UAH', str(date_and_currencies[1]) + ', ' + str(date_and_currencies[0]))
