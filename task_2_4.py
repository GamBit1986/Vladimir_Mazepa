def convert_name_extract(list_in: list) -> list:
    """Извлекает имена из элементов и формирует список приветствий."""
    list_out = []
    i = 0
    for text in list_in:
        text1 = text
        # print(text1)
        parts = text1.split(' ')
        # print(parts)
        text2 = (parts.pop()).capitalize()
        # print(text2)
        list_out.append(text2)
    # print(list_out)
    for name in list_out:
        greeting = f'Привет, {name}!'
        # print(greeting)
        list_out[i] = greeting
        i += 1
    return list_out


my_list = ['инженер-конструктор Игорь', 'главный бухгалтер МАРИНА', 'токарь высшего разряда нИКОЛАй', 'директор аэлита']
result = convert_name_extract(my_list)
print(result)