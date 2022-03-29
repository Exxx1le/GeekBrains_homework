# 3.Склонение слова
# Реализовать склонение слова «процент» во фразе «N процентов». Вывести эту фразу на экран отдельной строкой
# для каждого из чисел в интервале от 1 до 100:
# 1 процент
# 2 процента
# 3 процента
# 4 процента
# 5 процентов
# 6 процентов
# ...
# 100 процентов

for percent in range(1, 101):
    if percent % 10 == 1 and percent != 11:
        print(percent, 'процент')
    elif percent == 12 or percent == 13 or percent == 14:
        print(percent, 'процентов')
    elif (percent % 10 == 2 or percent % 10 == 3 or percent % 10 == 4):
        print(percent, 'процента')
    else:
        print(percent, 'процентов')
