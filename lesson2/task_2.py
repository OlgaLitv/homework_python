"""2 Дан список:
['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']

Необходимо его обработать — обособить каждое целое число (вещественные не трогаем) кавычками (добавить
 кавычку до и кавычку после элемента списка, являющегося числом) и дополнить нулём до двух целочисленных
 разрядов:
['в', '"', '05', '"', 'часов', '"', '17', '"', 'минут', 'температура', 'воздуха', 'была', '"', '+05',
 '"', 'градусов']

Сформировать из обработанного списка строку:
в "05" часов "17" минут температура воздуха была "+05" градусов
"""

weather_list = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
index = 0
weather_list2 = []
weather_string = ""
for element in weather_list:
    is_integer = True
    for letter in element:
        if not (ord('0') <= ord(letter) <= ord('9') or element[0] == '-' or element[0]  == '+'):
            is_integer = False
    if (is_integer and element != ''):
        weather_list2.append('"')
        if (element[0] == '-' or element[0]  == '+'):
            weather_list2.append(element[0] + f'{int(element[1:]):02d}')
            weather_string += '"' + element[0] + f'{int(element[1:]):02d}' + '" '
        else:
            weather_list2.append(f'{int(element):02d}')
            weather_string += '"' + f'{int(element):02d}' + '" '
        weather_list2.append('"')
        index += 2
    else:
        weather_list2.append(element)
        weather_string += element + ' '
    index += 1
print('обработанный список:', weather_list2)
print('строка:', weather_string)