import csv
import sys

def show(*argv):
    '''Эта часть кода, чтобы получить аргументы и командной строки'''
    _lst_arg = []
    _lst_arg_temp = []
    lst_arg = []
    for i in list(*argv):
        _lst_arg.append(i)

    _lst_arg_temp = _lst_arg[1:]

    arg = ''.join(_lst_arg_temp)
    lst_arg = arg.split(',')
    """В этой части кода проверяем сколько дано аргументов и в зависимости от количества выводим в соответсвии с заданием"""
    i = 0

    for num in lst_arg:
        i += 1

    if lst_arg == [""]:

        with open('bakery.csv', newline='', encoding='utf-8') as f:
            reader = csv.reader(f)
            for row in reader:
                print(row[1])
    elif i == 1:

        with open('bakery.csv', newline='', encoding='utf-8') as f:
            _lst_out = []
            index = int(lst_arg[0]) - 1
            lst_out = []
            reader = csv.reader(f)
            for row in reader:
                _lst_out.extend(row)
            lst_out.extend(_lst_out[1::2])
            for num in lst_out[index:]:
                print(num)
    elif i == 2:

        for num in argv:
            lst_arg.append(num)
        _lst_out = []
        index1 = int(lst_arg[0]) - 1
        index2 = int(lst_arg[1])
        lst_out = []

        with open('bakery.csv', newline='', encoding='utf-8') as f:
            reader = csv.reader(f)
            for row in reader:
                _lst_out.extend(row)
            lst_out.extend(_lst_out[1::2])
            """Эти if для проверки, если ввели правильные числа, но наоборот"""
            if lst_arg[0] > lst_arg[1]:
                index1 = int(lst_arg[1]) - 1
                index2 = int(lst_arg[0])
                for i in lst_out[index1:index2]:
                    print(i)
            elif lst_arg[0] < lst_arg[1]:
                index1 = int(lst_arg[0]) - 1
                index2 = int(lst_arg[1])
                for i in lst_out[index1:index2]:
                    print(i)
    else:
        print('Неверно заданы индексы')

    return 0

if __name__ == '__main__':
    exit(show(sys.argv))