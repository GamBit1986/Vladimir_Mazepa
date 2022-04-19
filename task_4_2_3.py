import requests
from datetime import datetime

def currency_rates(code: str) -> float:
    """возвращает курс валюты `code` по отношению к рублю"""
    list_temp_sec = []
    list_temp_third = []
    money = []

    list_temp_val_2 = []
    list_temp_val_3 = []
    value = []

    # result = []

    code = code.upper()
    print(code)
    r = requests.get('http://www.cbr.ru/scripts/XML_daily.asp').text


    # Эта часть кода отрезает списки по названия валют

    list_temp = r.split("</CharCode>")

    for k in list_temp:
        list_temp_sec.append(k.split("<"))

    i = 0
    while i < len(list_temp_sec)-1:
        list_temp_third.append(list_temp_sec[i][:1:-1][:1:])
        i += 1

    i = 0
    for elem in list_temp_third:
        money.append(elem[i][::-1][:3][::-1])

    # Здесь делаем то же самое с курсовой стоимостью

    list_temp_val = r.split("</Value>")
    for k in list_temp_val:
        list_temp_val_2.append(k.split("<"))

    i = 0
    while i < len(list_temp_val_2)-1:
        list_temp_val_3.append(list_temp_val_2[i][:1:-1][:1:])
        i += 1

    i = 0
    for elem in list_temp_val_3:
        value.append(elem[i].strip('Value>'))

    # Проверяем на совпадение, если найдено, то выводим значение, иначе- возвращаем None

    i = 0
    for mon in money:
        i += 1
        if mon == code:
            result_value = float(value[i-1].replace(',', '.'))
            break
        else:
            result_value = None

    # Находим дату и конвертируем в формат datetime

    temp_date = (((r.split(" name")[:1])[0])[::-1][:11][::-1]).strip('"')
    today = datetime.strptime(temp_date, "%d.%m.%Y")
    print(today, type(today))

    return result_value
    """Как вывести формат datetime в кортеж в нормальном виде, не разобрался, времени не хватило, пока выоводит, но в виде: datetime.datetime(d:19, m:04...."""

print(currency_rates("USD"), type(currency_rates("USD")))
print(currency_rates("noname"))
print(currency_rates("eur"))
print(currency_rates("sek"))