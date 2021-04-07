"""4. Написать скрипт, который выводит статистику для заданной папки в виде словаря, в котором ключи —
верхняя граница размера файла (пусть будет кратна 10), а значения — общее количество файлов (в том числе и
в подпапках), размер которых не превышает этой границы, но больше предыдущей (начинаем с 0), например:
    {
      100: 15,
      1000: 3,
      10000: 7,
      100000: 2
    }
Тут 15 файлов размером не более 100 байт; 3 файла больше 100 и не больше 1000 байт...
Подсказка: размер файла можно получить из атрибута .st_size объекта os.stat."""

import os
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
    print('{')
    for number in sorted(dict_files):
        print(f'{number}: {len(dict_files[number])},')
    print('}')


if __name__ == '__main__':
    import sys
    exit(main(sys.argv))
