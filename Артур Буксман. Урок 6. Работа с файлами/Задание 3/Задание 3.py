# 3. Есть два файла: в одном хранятся ФИО пользователей сайта, а в другом — данные об их хобби.
# Известно, что при хранении данных используется принцип: одна строка — один пользователь,
# разделитель между значениями — запятая. Написать код, загружающий данные из обоих файлов
# и формирующий из них словарь: ключи — ФИО, значения — данные о хобби. Сохранить словарь
# в файл. Проверить сохранённые данные. Если в файле, хранящем данные о хобби, меньше
# записей, чем в файле с ФИО, задаём в словаре значение None. Если наоборот — выходим из
# скрипта с кодом «1». При решении задачи считать, что объём данных в файлах во много раз
# меньше объема ОЗУ.
import json

with open('task_3_users.txt', 'r', encoding='utf-8') as f:
    with open('task_3_hobbies.txt', 'r', encoding='utf-8') as file:
        with open('dict.json', 'w', encoding='utf-8') as save_file:
            users = [i.split(',')[0] for i in f.readlines()]
            hobbies = [i.split(',')[0] for i in file.readlines()]
            if len(hobbies) < len(users):
                hobbies += (len(users) - len(hobbies)) * [None]
            hobbies_dict = dict(zip(users, hobbies))

            json_dict = json.dumps(hobbies_dict, ensure_ascii=False)
            save_file.write(json_dict)

        if len(hobbies) > len(users):
            raise Exception('Process finished with exit code 1')
