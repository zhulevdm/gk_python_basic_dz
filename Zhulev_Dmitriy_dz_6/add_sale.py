import sys


def add_sale(argv):
    program, arg = argv
    with open('bakery.csv', 'a', encoding='utf-8') as fw:
        fw.write(arg + '\n')
    return 0


exit(add_sale(sys.argv))
