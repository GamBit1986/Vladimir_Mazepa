import sys
import json


def prepare_dataset(path_users_file: str, path_hobby_file: str) -> dict:
    """
    Считывает данные из файлов и возвращает словарь, где:
        ключ — ФИО, значение — данные о хобби (список строковых переменных)
    :param path_users_file: путь до файла, содержащий ФИО пользователей, разделенных запятой по строке
    :param path_hobby_file: путь до файла, содержащий хобби, разделенные запятой по строке
    :return: Dict(str: Union[List[str]|None])
    """

    '''Удаляем все лишнее, получаем чистые списки'''
    with open('users.csv', 'r', encoding='utf-8') as file_1:
        users = file_1.readlines()
        users_clear = list(map(lambda el: el.replace('\n', '').replace(',', ' '), users))


    with open('hobby.csv', 'r', encoding='utf-8') as file_2:
        hobby = file_2.readlines()
        hobby_clear = list(map(lambda el: el.replace('\n', ''), hobby))

    '''Проверяем условие количества элементов в списках'''
    if len(users_clear) < len(hobby_clear):
        sys.exit(1)

    while len(users_clear) > len(hobby_clear):
        hobby_clear.append(None)

    """Создаем словарь и возвращаем его"""
    dict_out = dict(zip(users_clear, hobby_clear))
    return dict_out  # верните словарь, либо завершите исполнение программы кодом 1

# заполнение файлов
users_lines = ['Иванов,Иван,Иванович\nПетров,Петр,Петрович\nСидоров,Сидр,Сидрович']
with open('users.csv', 'w', encoding='utf-8') as f:
    f.writelines(users_lines)

hobby_lines = ['скалолазание,охота\nгорные лыжи']
with open('hobby.csv', 'w', encoding='utf-8') as f:
    f.writelines(hobby_lines)

# вывод результата в файл json
dict_out = prepare_dataset('users.csv', 'hobby.csv')
with open('task_6_3_result.json', 'w', encoding='utf-8') as fw:
    json.dump(dict_out, fw, ensure_ascii=False, indent=2)