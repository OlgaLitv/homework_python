"""5. ** (вместо 4) Решить задачу 4 и реализовать интерфейс командной строки, чтобы можно было задать
путь к обоим исходным файлам и путь к выходному файлу со словарём. Проверить работу скрипта для случая,
когда все файлы находятся в разных папках."""


def main(argv):
    try:
        file_us = argv[1]
        file_ho = argv[2]
        file_out = argv[3]
    except IndexError:
        print('give 3 files names, please')
        exit(1)
    dct = {}
    try:
        file_users = open(file_us, 'r', encoding='utf-8')
        file_hobby = open(file_ho, 'r', encoding='utf-8')
        write_file = open(file_out, 'x', encoding='utf-8')
    except FileNotFoundError:
        print("Can't open file")
        exit(1)

    for us_line in file_users:
        hob_line = file_hobby.readline()
        us_line = us_line.rstrip()
        if hob_line:
            dct[us_line] = hob_line.rstrip()
            write_file.write(us_line + ':' + hob_line.rstrip() + '\n')
        else:
            dct[us_line] = ['None']
            write_file.write(us_line + ':None\n')
    hob_line = file_hobby.readline()
    file_users.close()
    file_hobby.close()
    write_file.close()
    if hob_line:
        exit(1)
    return 0


if __name__ == '__main__':
    import sys
    exit(main(sys.argv))
