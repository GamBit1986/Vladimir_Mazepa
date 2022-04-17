import requests
from bs4 import BeautifulSoup
from datetime import datetime as dt
import json
import re
from re import sub
from decimal import Decimal
import io
from datetime import datetime
import pandas as pd
i = 0
list_temp_sec = []

def currency_rates(code: str) -> float:
    """возвращает курс валюты `code` по отношению к рублю"""

    r = requests.get('http://www.cbr.ru/scripts/XML_daily.asp').text
    print(type(r))
    print(r)
    list_temp = r.split("</CharCode>")
    print(list_temp)
    for i in list_temp:
        list_temp_sec.append(i.split("<"))
    print(list_temp_sec)
    for i in list
    # print(convert)

    result_value = 1.11  ## здесь должно оказаться результирующее значение float
    return result_value


print(currency_rates("USD"))
# print(currency_rates("noname"))