# 1. Реализовать вывод информации о промежутке времени в зависимости от его продолжительности duration в секундах:

# до минуты: <s> сек
duration = int(input('Введите время до 1 минуты в секундах '))
if duration < 60:
    print(duration, 'сек')
else:
    print('Введенное время больше 1 минуты')

# до часа: <m> мин <s> сек
duration = int(input('Введите время до 1 часа в секундах '))
if duration < 60:
    print(duration, 'сек')
elif duration >= 60 and duration < 3600:
    minutes = duration // 60
    seconds = duration % 60
    print(minutes, 'мин', seconds, 'сек')
else:
    print('Введенное время больше 1 часа')

# до суток: <h> час <m> мин <s> сек
duration = int(input('Введите время до 1 суток в секундах '))
if duration < 60:
    print(duration, 'сек')
elif duration >= 60 and duration < 3600:
    minutes = duration // 60
    seconds = duration % 60
    print(minutes, 'мин', seconds, 'сек')
elif duration >= 3600 and duration < 86400:
    hours = duration // 3600
    minutes = duration % 3600 // 60
    seconds = (duration % 3600) % 60
    print(hours, 'час', minutes, 'мин', seconds, 'сек')
else:
    print('Введенное время больше 1 cуток')
