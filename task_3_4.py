
def thesaurus_adv(*args: str) -> dict:
    char_str = str(args)
    list_of_chars = list(char_str)
    list_args = list(args)
    list_name_surname = []
    k = 1
    l = 0
    list_of_letters = []
    dict_out = {}
    dict_out_temp = {}

    for i in list_of_chars:
        if i.isupper():
            list_of_letters.append(i)

    for j in list_args:
        list_name_surname.append(j.split(" "))


    for element in list_name_surname:
        element.extend(list_of_letters[k])
        element.extend(list_of_letters[k-1])
        k += 2

    for element in list_name_surname:
        dict_out_temp.setdefault(element[3], []).append(str(element[0:2]))
    print(dict_out_temp)
    for element in list_name_surname:
        dict_out.setdefault(element[2], {})

    # for val in dict_out_temp.values():
    #     print(val)



    print(list_name_surname)
    # print(dict_out)
    # print(dict_out_temp)
    # print(dict_out_temp.values())





thesaurus_adv("Иван Сергеев", "Инна Серова", "Петр Алексеев", "Илья Иванов", "Анна Савельева")

