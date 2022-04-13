def thesaurus(*args) -> dict:
    """Функция обрабатывает входящие имена и возвращает словарь, ключем которого является первая буква"""
    char_str = str(args)
    list_of_names = list(args)
    upper_list = []
    list_out = []
    dict_out = {}

    for text in char_str:
        text1 = text
        if text1.isupper():
            upper_list.append(text1)

    for letter, name in zip(upper_list, list_of_names):
        temp = (f'{letter}, {name}').split(', ')
        list_out.append(temp)

    for pair in list_out:
        dict_out.setdefault(pair[0], []).append(pair[1])

    return dict_out


print(thesaurus("Иван", "Мария", "Петр", "Илья", "Зинаида", "Зульфия"))

