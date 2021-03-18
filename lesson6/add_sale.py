"""Данные хранить в файле bakery.csv в кодировке utf-8. Нумерация записей начинается с 1. Примеры запуска
скриптов:"""


def main(argv):
    try:
        sale = argv[1]
    except IndexError:
        print('input number, please')
        exit(1)

    sale = '000000000000' + sale
    with open('bakery.csv', 'a', encoding='utf-8') as f:
        f.write(sale[len(sale)-12:] + '\n')


if __name__ == '__main__':
    import sys
    exit(main(sys.argv))
