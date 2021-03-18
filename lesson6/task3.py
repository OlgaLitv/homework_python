"""3. Есть два файла: в одном хранятся ФИО пользователей сайта, а в другом — данные об их хобби. Известно,
что при хранении данных используется принцип: одна строка — один пользователь, разделитель между
значениями — запятая. Написать код, загружающий данные из обоих файлов и формирующий из них словарь: ключи — ФИО,
значения — данные о хобби. Сохранить словарь в файл. Проверить сохранённые данные. Если в файле, хранящем данные
о хобби, меньше записей, чем в файле с ФИО, задаём в словаре значение None. Если наоборот — выходим из скрипта
с кодом «1». При решении задачи считать, что объём данных в файлах во много раз меньше объема ОЗУ.
Фрагмент файла с данными о пользователях (users.csv):
Иванов,Иван,Иванович
Петров,Петр,Петрович
Фрагмент файла с данными о хобби (hobby.csv):
скалолазание,охота
горные лыжи"""


dct = {}
file_users = open('users.csv', 'r', encoding='utf-8')
file_hobby = open('hobby.csv', 'r', encoding='utf-8')
users = file_users.read().split('\n')
hobby = file_hobby.read().split('\n')
l_hobby = len(hobby)
for i in range(len(users)):
    if i < l_hobby:
        dct[users[i]] = hobby[i]
    else:
        dct[users[i]] = None

with open('for_task3.txt', 'w', encoding='utf-8') as f:
    # сохраняем в файл
    for key, item in dct.items():
        if item:
            f.write(key + ':' + item + '\n')
        else:
            f.write(key + ':None\n')

dct = {}
with open('for_task3.txt', 'r', encoding='utf-8') as f:
    content = f.read().split('\n')
    # проверка сохраненных данных - загружаем их и выводим на печать
    for item in content:
        if item != '':
            user_and_hobby = item.split(':')
            dct[user_and_hobby[0]] = user_and_hobby[1]
print(dct)
if l_hobby > len(users):
    exit(1)
