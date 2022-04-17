# 1. Не используя библиотеки для парсинга, распарсить (получить определённые данные) файл логов
# web-сервера nginx_logs.txt
# (https://github.com/elastic/examples/raw/master/Common%20Data%20Formats/nginx_logs/nginx_logs)
# — получить список кортежей вида:
# ('141.138.90.60', 'GET', '/downloads/product_2')

with open('nginx_logs.txt', 'r', encoding='utf-8') as f:
    for i in f.readlines():
        ip = (i.split('-')[0])
        request_type = (i.split('"')[1][0:3])
        request_url = (i.split('"')[1][4:24])
        request_tuple = (ip, request_type, request_url)
        print(request_tuple)
