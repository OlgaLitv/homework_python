"""5. * (вместо 4) Написать скрипт, который выводит статистику для заданной папки в виде словаря, в котором
ключи те же, а значения — кортежи вида (<files_quantity>, [<files_extensions_list>]), например:
  {
      100: (15, ['txt']),
      1000: (3, ['py', 'txt']),
      10000: (7, ['html', 'css']),
      100000: (2, ['png', 'jpg'])
    }
Сохраните результаты в файл <folder_name>_summary.json в той же папке, где запустили скрипт."""


import os
import json
from collections import defaultdict


def main(argv):
    if len(argv) != 2:
        print('Введите папку')
        exit(1)

    root_dir = argv[1]
    dict_files = defaultdict(list)
    for root, dirs, files in os.walk(root_dir):
        for file in files:
            size = os.path.getsize(os.path.join(root, file))
            num = len(str(size))
            dict_files[10 ** num].append(file)
    dict_to_save = {}
    for number in sorted(dict_files):
        set_ext = set()
        for file in dict_files[number]:
            _, ext = os.path.splitext(file)
            set_ext.add(ext[1:])
        dict_to_save[number] = tuple((len(dict_files[number]), list(set_ext)))
    cur_dir = os.path.abspath(os.curdir)
    file_save_name = os.path.basename(cur_dir) + '_summary.json'
    string_dict = json.dumps(dict_to_save)
    with open(file_save_name, 'w', encoding='utf8') as f:
        f.write(string_dict)


if __name__ == '__main__':
    import sys
    exit(main(sys.argv))
