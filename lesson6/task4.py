"""4. * (вместо 3) Решить задачу 3 для ситуации, когда объём данных в файлах превышает объём ОЗУ
(разумеется, не нужно реально создавать такие большие файлы, это просто задел на будущее проекта). Также
реализовать парсинг данных из файлов - получить отдельно фамилию, имя и отчество для пользователей и название
каждого хобби: преобразовать в какой-нибудь контейнерный тип (список, кортеж, множество, словарь). Обосновать
выбор типа. Подумать, какие могут возникнуть проблемы при парсинге. В словаре должны храниться данные, полученные
в результате парсинга."""


hob_line = ''
dct = {}
with open('users.csv', 'r', encoding='utf-8') as file_users, open('hobby.csv', 'r', encoding='utf-8') as file_hobby, \
        open('for_task4.txt', 'w', encoding='utf-8') as write_file:
    for us_line in file_users:
        hob_line = file_hobby.readline()
        # ФИО преобразуем в кортеж, так как будем их использовать в качестве ключа словаря
        # а хобби можно хранить в виде списка, вдруг понадобится редактировать. Логично вместо None делать
        # пустой список, но по условию должно быть None
        us_line = us_line.rstrip()
        us_line1 = tuple(us_line.split(','))
        if hob_line:
            dct[us_line1] = hob_line.rstrip().split(',')
            write_file.write(us_line + ':' + hob_line.rstrip() + '\n')
        else:
            dct[us_line1] = [None]
            write_file.write(us_line + ':None\n')
    hob_line = file_hobby.readline()
print(dct)
if hob_line:
    exit(1)
