""" *(вместо задачи 2) Решить задачу 2 не создавая новый список (как говорят, in place).
Эта задача намного серьёзнее, чем может сначала показаться."""

weather_list = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
index = 0
weather_string = ""
while index < len(weather_list):
    is_integer = True
    element = weather_list[index]
    for letter in element:
        if not (ord('0') <= ord(letter) <= ord('9') or element[0] == '-' or element[0] == '+'):
            is_integer = False
    if is_integer and element != '':
        if element[0] == '-' or element[0] == '+':
            weather_list[index] = element[0] + f'{int(element[1:]):02d}'
            weather_string += '"' + weather_list[index] + '" '
        else:
            weather_string += '"' + f'{int(element):02d}' + '" '
        weather_list.insert(index, '"')
        weather_list.insert(index+2, '"')
        index += 2
    else:
        weather_string += element + ' '
    index += 1
print('обработанный список:', weather_list)
print('строка:', weather_string)
