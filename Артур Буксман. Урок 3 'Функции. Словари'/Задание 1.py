# 1. Написать функцию num_translate(), переводящую числительные от 0 до 10 c английского на русский язык. Например:
# >>> num_translate("one")
# "один"
# >>> num_translate("eight")
# "восемь"

def num_translate(eng_number):
    num_dict = {'null': 'ноль', 'one': 'один', 'two': 'два', 'three': 'три', 'four': 'четыре', 'five': 'пять',
                'six': 'шесть', 'seven': 'семь', 'eight': 'восемь', 'nine': 'девять', 'ten': 'десять'}
    return num_dict.get(eng_number)  # можно также написать num_dict[eng_number]


print(num_translate('two'))
