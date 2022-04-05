# 5. Реализовать функцию get_jokes(), возвращающую n шуток, сформированных из трех
# случайных слов, взятых из трёх списков (по одному из каждого):
# nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
# adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
# adjectives = ["веселый", "яркий", "зеленый", "утопичный",
# "мягкий"]
# Например:
# >>> get_jokes(2)
# ["лес завтра зеленый", "город вчера веселый"]
# Документировать код функции.
# Сможете ли вы добавить еще один аргумент — флаг, разрешающий или запрещающий повторы
# слов в шутках (когда каждое слово можно использовать только в одной шутке)? Сможете ли вы
# сделать аргументы именованными?

import random


def get_jokes(count, repeat=True):
    """
    :param count: amount of jokes to print,
    :param repeat: repeat words in jokes, default=True
    """
    nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
    adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
    adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]

    if repeat is True:
        a = random.choices(nouns, k=count)
        b = random.choices(adverbs, k=count)
        c = random.choices(adjectives, k=count)
    else:
        a = random.sample(nouns, k=count)
        b = random.sample(adverbs, k=count)
        c = random.sample(adjectives, k=count)

    for noun, adverb, adjective in zip(a, b, c):
        print(f'{noun} {adverb} {adjective}')


get_jokes(3)
get_jokes(3, repeat=False)
