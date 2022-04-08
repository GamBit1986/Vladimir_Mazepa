# Задача 2
def convert_list_in_str(list_in: list) -> str:
    # """Обособляет каждое целое число кавычками, добавляя кавычку до и после элемента
    #     списка, являющегося числом, и дополняет нулём до двух целочисленных разрядов.
    #     Формирует из списка результирующую строковую переменную и возвращает."""
    list_out = []
    i = 0
    for elem in list_in:
        if elem.isdigit() == True:
            if int(elem) <= 9:
                list_out.append('"')
                list_out.append('0' + str(elem))
                list_out.append('"')
            elif int(elem) > 9:
                list_out.append('"')
                list_out.append(str(elem))
                list_out.append('"')
            else:
                list_out.append(str(elem))
        elif elem == "+5":
            list_out.append('"')
            list_out.append('+05')
            list_out.append('"')
        else:
            list_out.append(elem)
    print(list_out)
        # print(type(elem))


    str_out = ' '.join(list_out)
    return str_out


my_list = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']

result = convert_list_in_str(my_list)
print(result)