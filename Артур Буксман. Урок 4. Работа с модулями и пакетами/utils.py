import requests
from decimal import Decimal


def currency_rates(cur_code):
    response = requests.get('http://www.cbr.ru/scripts/XML_daily.asp')

    value_dict = {}

    for i in response.text.split('<CharCode>')[1:]:
        value = i.split('Value')[1]
        a, b = value.split(',')
        numbers = Decimal(f'{a[1:3]}.{b[0:4]}')
        value_dict.setdefault(i[0:3], numbers)

    return value_dict.get(cur_code)
