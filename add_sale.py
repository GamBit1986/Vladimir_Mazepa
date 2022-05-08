import csv
import sys

def add_sales(argv: float):
    '''Функция добавляет стоимость продажи в файл CSV'''

    with open('bakery.csv', 'r', newline='', encoding='utf-8') as csvfile:
        line_count = 0
        for row in csvfile:
            line_count += 1
        print(f'Processed {line_count} lines.')

    with open('bakery.csv', 'a', encoding='utf-8') as csvfile:
        csvfile.write(str(line_count + 1) + ',' + str(argv[1]) + '\n')

    return 0

if __name__ == '__main__':
    exit(add_sales(sys.argv))