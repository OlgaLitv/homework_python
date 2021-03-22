"""Для чтения данных реализовать в командной строке следующую логику:
. просто запуск скрипта — выводить все записи;
. запуск скрипта с одним параметром-числом — выводить все записи с номера, равного этому числу, до конца;
. запуск скрипта с двумя числами — выводить записи, начиная с номера, равного первому числу, по номер,
равный второму числу, включительно.
Подумать, как избежать чтения всего файла при реализации второго и третьего случаев.
Данные хранить в файле bakery.csv в кодировке utf-8. Нумерация записей начинается с 1."""


def main(argv):
    l_argv = len(argv)
    sale_len = 14
    with open('bakery.csv', 'r', encoding='utf-8') as f:
        # ставим указатель файла на конец, чтобы узнать размер файла
        f.seek(0, 2)
        file_size = f.tell()
        f.seek(0)
        if l_argv == 1:
            # показать все записи
            for line in f:
                print(float(line.rstrip()))
        elif l_argv == 2:
            # выводить все записи с номера, равного этому числу, до конца
            num = (int(argv[1]) - 1) * sale_len
            if num < file_size or num < 0:
                f.seek(num)
                lines = f.readlines()
                for line in lines:
                    if line != '':
                        print(float(line.rstrip()))
            else:
                print('index out of range')
        elif l_argv == 3:
            # выводить записи, начиная с номера, равного первому числу, по номер,
            # равный второму числу, включительно
            start = int(argv[1])-1
            finish = int(argv[2])
            if start > finish or finish * sale_len > file_size or start < 0:
                print('input correct data')
            else:
                f.seek(start * sale_len)
                for i in range(finish - start):
                    content = f.readline()
                    if i != '':
                        print(float(content))


if __name__ == '__main__':
    import sys
    exit(main(sys.argv))
