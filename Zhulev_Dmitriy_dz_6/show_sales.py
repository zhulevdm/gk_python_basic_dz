import sys


def show_sales(argv):
    program, *args = argv
    with open('bakery.csv', 'r', encoding='utf-8') as fr:
        cnt_str = len(fr.readlines())
        fr.seek(0)
        if len(args) == 0:
            print(fr.read().strip())
        elif len(args) == 1:
            lines = fr.readlines()
            for i in range(int(args[0])-1, cnt_str):
                print(lines[i].strip())
        else:
            lines = fr.readlines()
            for i in range(int(args[0])-1, int(args[1])):
                print(lines[i].strip())
    return 0


exit(show_sales(sys.argv)) 
