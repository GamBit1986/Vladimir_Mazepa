

def num_translate(in_put: str) -> str:
    """переводит числительное с английского на русский """
    number = {
        'zero': 'ноль',
        'one': 'один',
        'two': 'два',
        'three': 'три',
        'four': 'четыре',
        'five': 'пять',
        'six': 'шесть',
        'seven': 'семь',
        'eight': 'восемь',
        'nine': 'девять',
        'ten': 'десять',
        'Zero': 'Ноль',
        'One': 'Один',
        'Two': 'Два',
        'Three': 'Три',
        'Four': 'Четыре',
        'Five': 'Пять',
        'Six': 'Шесть',
        'Seven': 'Семь',
        'Eight': 'Восемь',
        'Nine': 'Девять',
        'Ten': 'Десять'
    }


    str_out_= number.get(in_put, 'Введенное число не входит в диапазон от 0 до 10.')
    str_out = f' Перевод введенного числа: {str_out_}'
    return str_out


print(num_translate("One"))
print(num_translate("eight"))
print(num_translate("Zero"))
print(num_translate("eleven"))