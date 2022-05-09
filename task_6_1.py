from pprint import pprint


def get_parse_attrs(line: str) -> tuple:
    """Парсит строку на атрибуты и возвращает кортеж атрибутов (<remote_addr>, <request_type>, <requested_resource>)  ('141.138.90.60', 'GET', '/downloads/product_2'),"""
    _paragraphs = []
    paragraph = []
    remote_addr = []
    request_type = []
    requested_resource = []
    list_out = []
    with open(line, 'r', encoding='utf-8') as file_1:
        for line in file_1:
            _paragraphs.extend(line.split(' ')[0:1])
            _paragraphs.extend(line.split(' ')[5:7])
        for elem in _paragraphs:
            elem = elem.strip('"')
            paragraph.append(elem.strip('"'))

        remote_addr.extend(paragraph[::3])
        request_type.extend(paragraph[1::3])
        requested_resource.extend(paragraph[2::3])

        for data in zip(remote_addr, request_type, requested_resource):
            list_out.append(data)

        pprint(list_out)
    return list_out  

get_parse_attrs('nginx_logs.txt')


