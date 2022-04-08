from random import uniform


def transfer_list_in_str(list_in: list) -> str:
    """Преобразует каждый элемент списка (вещественное число) в строку вида '<r> руб <kk> коп' и
        формирует из них единую строковую переменную разделяя значения запятой."""
    list_out = []
    i = 0
    for number in list_in:
        list_out.append(int(number // 1))
        list_out.append(round((number % 1) * 100))
    # print(list_out)
    while i < len(list_out):
        if i % 2 == 0 or i == 0:
            if list_out[i] < 10:
                list_out[i] = '0' + str(list_out[i]) + ' руб ' + str(list_out[i + 1]) + ' копеек'
            elif list_out[i + 1] < 10:
                list_out[i] = str(list_out[i]) + ' руб ' + '0' + str(list_out[i + 1]) + ' копеек'
            else:
                list_out[i] = str(list_out[i]) + ' руб ' + str(list_out[i + 1]) + ' копеек'
        i += 1
    list_out = list_out[::2]
    # print(list_out)

    str_out = ', '.join(list_out)
    return str_out


my_list = [round(uniform(0, 100), 2) for _ in range(1, 16)]  # автоматическая генерация случайных 15 чисел
print(f'Исходный список: {my_list}')
result_1 = transfer_list_in_str(my_list)
print(f'Полученная строка: {result_1}')


def sort_prices(list_in: list) -> list:
    """Сортирует вещественные числа по возрастанию, не создавая нового списка"""
    list_id = id(list_in)
    print(f'Номер ячейки памяти входящего списка: {list_id}')
    list_in.sort()

    return list_in


# зафиксируйте здесь информацию по исходному списку my_list
result_2 = sort_prices(my_list)
# зафиксируйте здесь доказательство, что результат result_2 остался тем же объектом
result_2_id = id(result_2)
print(f'Отсортированная строка: {result_2}', f'Номер ячейки памяти отсортированного списка: {result_2_id}')


def sort_price_adv(list_in: list) -> list:
    """Создаёт новый список и возвращает список с элементами по убыванию"""
    print(f'Входящий на сортировку в порядке убывания список: {list_in}')
    list_out = sorted(list_in, reverse=True)
    return list_out

list_in_id = id(my_list)
result_3 = sort_price_adv(my_list)
result_3_id = id(result_3)
print(f'Отсортированный в порядке убывания список: {result_3}')
print(f'id отсортированной в порядке убывания строки: {result_3_id}', f'Номер ячейки памяти входящего списка: {list_in_id}')


def check_five_max_elements(list_in: list) -> list:
    """Проверяет элементы входного списка вещественных чисел и возвращает
        список из ПЯТИ максимальных значений"""
    # print(list_in)
    list_in.sort()
    print(f'Отсортированный в порядке возрастания список: {list_in}')
    list_out = []
    i = 0
    while i < 5:
        cur_max = list_in.pop()
        list_out.append(cur_max)
        i += 1
    return list_out


result_4 = check_five_max_elements(my_list)
print(f'Список из пяти максимальных значений: {result_4}')