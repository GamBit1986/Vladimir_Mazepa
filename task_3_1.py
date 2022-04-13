

def num_translate(value: str) -> str:
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
        'ten': 'десять'
    }

    str_out_= number.get(value, 'Введенное число не входит в диапазон от 0 до 10.')
    str_out = f' Перевод введенного числа: {str_out_}'
    return str_out


print(num_translate("one"))
print(num_translate("eight"))
print(num_translate("zero"))
print(num_translate("eleven"))