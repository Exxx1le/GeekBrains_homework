# 2. Написать функцию currency_rates(), принимающую в качестве аргумента код валюты (например, USD, EUR, GBP, ...)
# и возвращающую курс этой валюты по отношению к рублю. Использовать библиотеку requests. В качестве API можно
# использовать http://www.cbr.ru/scripts/XML_daily.asp. Рекомендация: выполнить предварительно запрос к API в обычном
# браузере, посмотреть содержимое ответа. Можно ли, используя только методы класса str, решить поставленную задачу?
# Функция должна возвращать результат числового типа, например float. Подумайте: есть ли смысл для работы с денежными
# величинами использовать вместо float тип Decimal? Сильно ли усложняется код функции при этом? Если в качестве
# аргумента передали код валюты, которого нет в ответе, вернуть None. Можно ли сделать работу функции не зависящей
# от того, в каком регистре был передан аргумент? В качестве примера выведите курсы доллара и евро.
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


print(currency_rates('USD'))
print(currency_rates('EUR'))
