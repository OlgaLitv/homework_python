"""3. Создать структуру файлов и папок, как написано в задании 2 (при помощи скрипта или «руками»
в проводнике). Написать скрипт, который собирает все шаблоны в одну папку templates, например:
|--my_project
   ...
  |--templates
   |   |--mainapp
   |   |  |--base.html
   |   |  |--index.html
   |   |--authapp
   |      |--base.html
   |      |--index.html
Примечание: исходные файлы необходимо оставить; обратите внимание, что html-файлы расположены в родительских
папках (они играют роль пространств имён); предусмотреть возможные исключительные ситуации; это реальная задача,
которая решена, например, во фреймворке django"""
import os
import shutil

cur_dir = os.path.join(os.path.abspath(os.curdir), 'my_project')
new_dir = os.path.join(cur_dir, 'templates')
if not os.path.exists(new_dir):
    os.mkdir(new_dir)
for root, dirs, files in os.walk(cur_dir):
    path = root.split(os.sep)
    try:
        old_dir = os.sep.join(path[path.index('templates')+1:])
        new_subdir = os.path.join(new_dir, old_dir)
        if not os.path.exists(new_subdir):
            # папка
            os.mkdir(new_subdir)
        for file in files:
            old_file, new_file = os.path.join(root, file), os.path.join(new_subdir, file)
            if not os.path.exists(new_file):
                # файл
                open(new_file, 'w', encoding='utf-8')
                shutil.copyfile(old_file, new_file)
    except ValueError:
        # нет 'templates' в пути, значит, идем дальше
        pass
