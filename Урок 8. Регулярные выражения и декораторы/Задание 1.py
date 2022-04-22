# 1. Написать функцию email_parse(<email_address>), которая при помощи регулярного выражения извлекает
# имя пользователя и почтовый домен из email адреса и возвращает их в виде словаря. Если адрес не валиден,
# выбросить исключение ValueError. Пример:
# >>> email_parse('someone@geekbrains.ru')
# {'username': 'someone', 'domain': 'geekbrains.ru'}
# >>> email_parse('someone@geekbrainsru')
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
#   ...
#     raise ValueError(msg)
# ValueError: wrong email: someone@geekbrainsru
import re


def email_parse(text):
    pattern = re.compile(r'\w+@\w+\.\w{2}')
    email_dict = {}

    if not pattern.findall(text):
        raise ValueError(f'wrong e-mail: {text}')
        exit(1)
    else:
        for i in pattern.findall(text):
            email_dict.setdefault('username', i.split('@')[0])
            email_dict.setdefault('domain', i.split('@')[1])
        return email_dict


print(email_parse('someone@geekbrains.ru'))
