

def main(argv):
    l_argv = len(argv)
    SALE_LEN = 14
    if l_argv == 1:
        # показать все записи
        with open('bakery.csv', 'r', encoding='utf-8') as f:
            for line in f:
                print(float(line.rstrip()))
    elif l_argv == 2:
        # выводить все записи с номера, равного этому числу, до конца
        num = int(argv[1]) - 1
        with open('bakery.csv', 'r', encoding='utf-8') as f:
            f.seek(SALE_LEN * num)
            lines = f.readlines()
            for line in lines:
                if line != '':
                    print(float(line.rstrip()))
    elif l_argv == 3:
        # выводить записи, начиная с номера, равного первому числу, по номер,
        # равный второму числу, включительно
        start = int(argv[1])-1
        finish = int(argv[2])
        with open('bakery.csv', 'r', encoding='utf-8') as f:
            f.seek(SALE_LEN * start)
            for i in range(finish - start):
                content = f.readline()
                if i != '':
                    print(float(content))


if __name__ == '__main__':
    import sys
    # from itertools import islice
    exit(main(sys.argv))
