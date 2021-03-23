"""2. * (вместо 1) Написать скрипт, создающий из config.yaml стартер для проекта со следующей структурой:
|--my_project
   |--settings
   |  |--__init__.py
   |  |--dev.py
   |  |--prod.py
   |--mainapp
   |  |--__init__.py
   |  |--models.py
   |  |--views.py
   |  |--templates
   |     |--mainapp
   |        |--base.html
   |        |--index.html
   |--authapp
   |  |--__init__.py
   |  |--models.py
   |  |--views.py
   |  |--templates
   |     |--authapp
   |        |--base.html
   |        |--index.html
Примечание: структуру файла config.yaml придумайте сами, его можно создать в любом текстовом редакторе
«руками» (не программно); предусмотреть возможные исключительные ситуации, библиотеки использовать нельзя.

******************************************

 Структура файла config.yaml выглядит так: корневая папка пишется без тире, вложенные в нее папки
с одним тире слева, вложенные во вложенные - с 2 тире и т.д., количество тире указывает на вложенность
my_project
-settings
--__init__.py
...
"""
# в файле config2.yaml валидная структура иерархии, но ее сложнее обрабатывать без библиотек: split-ом
# плохо делится (пробелы съедаются), еще иногда есть двоеточия в конце названия папки.
# И если прочитать библиотекой, тоже структура не из приятных: словарь с вложенными списками и словарями.
# получается, надо рекурсивно обходить и проверять тип элемента: список или словарь, чтобы узнать, каким
# методом обращаться. Вот как yaml.safe_load загружает эту структуру:
# {'my_project':
#  [{'settings': ['__init__.py', 'dev.py', 'prod.py']},
#   {'mainapp': ['__init__.py', 'models.py', 'views.py',
#              {'templates': ['mainapp', 'base.html', 'index.html']}]},
#   {'authapp': ['__init__.py', 'models.py', 'views.py',
#              {'templates': ['authapp', 'base.html', 'index.html']}]}]
# }
# Неужели действительно так хранят деревья?

import os


try:
    with open('config.yaml') as f:
        hier_dct = {0: ''}
        for line in f:
            line_lst = line.strip().split('-')
            lenght = len(line_lst)
            # в словаре hier_dct с ключом 0 хранится корневой путь (my_project), с ключом 1 - путь на 1 уровень глубже,
            # с ключом 2 - на 2 уровня глубже, чем корень, и т.д. Когда считываем очередную строку, то разделяем ее
            # split-ом по тире (строка без тире - корень, с 1 тире - папка в корневой, с 2 тире - папка, вложенная
            # в папку в корневой).
            # При этом в списке сначала тире, а последний элемент - название папки/файла.
            # И тогда путь относительно корня вычисляется так: количество тире указывает на степень вложенности папки
            # относительно корня, склеиваем путь на 1 уровень выше из hier_dict (по ключу длина списка минус 1) и
            # название папки/файла (это последний элемент списка). В словаре храним по 1 значению на ключ, то есть
            # затираем данные, если встретили папку mainapp после settings, чтобы всё вложенное в mainapp попало в нее,
            # а не в settings
            #
            file_name = os.path.join(hier_dct[lenght - 1], line_lst[lenght - 1])
            hier_dct[lenght] = file_name
            try:
                _, ext = os.path.splitext(file_name)
                if not os.path.exists(file_name) and ext == '':
                    os.makedirs(file_name)
                elif not os.path.exists(file_name) and ext != '':
                    open(file_name, 'w', encoding='utf-8')
            except PermissionError:
                print('Access denied')
except FileNotFoundError:
    print('File not found')
