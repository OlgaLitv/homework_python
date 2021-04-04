"""1. Написать скрипт, создающий стартер (заготовку) для проекта со следующей структурой папок:
|--my_project
   |--settings
   |--mainapp
   |--adminapp
   |--authapp
Примечание: подумайте о ситуации, когда некоторые папки уже есть на диске (как быть?); как лучше хранить
конфигурацию этого стартера, чтобы в будущем можно было менять имена папок под конкретный проект; можно ли
будет при этом расширять конфигурацию и хранить данные о вложенных папках и файлах (добавлять детали)?"""

import os

data = {'my_project': ['mainapp', 'adminapp', 'authapp']}
for key, lst_items in data.items():
    for item in lst_items:
        new_dir = os.path.join(key, item)
        if not os.path.exists(new_dir):
            os.makedirs(new_dir)
