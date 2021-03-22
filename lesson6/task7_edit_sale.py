"""7. * (вместо 6) Добавить возможность редактирования данных при помощи отдельного скрипта:
передаём ему номер записи и новое значение. При этом файл не должен читаться целиком — обязательное
требование. Предусмотреть ситуацию, когда пользователь вводит номер записи, которой не существует."""


def main(argv):
    try:
        sale_len = 14
        idx = (int(argv[1]) - 1) * sale_len
        sale = argv[2].rstrip()
        sale = '000000000000' + sale
    except IndexError:
        print('input number and sale, please')
        exit(1)

    with open('bakery.csv', 'r+', encoding='utf-8') as f:
        # ставим указатель файла на конец, чтобы узнать размер файла
        f.seek(0, 2)
        file_size = f.tell()
        if (idx < file_size) and (idx >= 0):
            f.seek(idx)
            f.write(sale[len(sale)-12:]+'\n')
        else:
            print('index out of range')


if __name__ == '__main__':
    import sys
    exit(main(sys.argv))
