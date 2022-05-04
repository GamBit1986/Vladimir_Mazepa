from pprint import pprint


def get_parse_attrs(line: str) -> tuple:
    """Парсит строку на атрибуты и возвращает кортеж атрибутов (<remote_addr>, <request_type>, <requested_resource>)  ('141.138.90.60', 'GET', '/downloads/product_2'),"""
    _paragraphs = []
    paragraph = []
    remote_addr = []
    request_type = []
    requested_resource = []
    with open(line, 'r', encoding='utf-8') as file_1:
        for line in file_1:
            _paragraphs.extend(line.split(' ')[0:1])
            _paragraphs.extend(line.split(' ')[5:7])
        for elem in _paragraphs:
            elem = elem.strip('"')
            paragraph.append(elem.strip('"'))
        for i, j, k in paragraph:
            remote_addr.append(i)
            request_type.append(j)
            requested_resource.append(k)
        print(*zip(remote_addr, request_type, requested_resource))
    return  # верните кортеж значений <remote_addr>, <request_type>, <requested_resource>

get_parse_attrs('nginx_logs.txt')
# list_out = list()
# with open('nginx_logs.txt', 'r', encoding='utf-8') as fr:
#     pass  # передавайте данные в функцию и наполняйте список list_out кортежами
#
# pprint(list_out)