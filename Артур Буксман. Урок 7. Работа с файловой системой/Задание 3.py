# Создать структуру файлов и папок, как написано в задании 2 (при помощи скрипта или
# «руками» в проводнике). Написать скрипт, который собирает все шаблоны в одну папку
# templates, например:
# |--my_project
# ...
# |--templates
# | |--mainapp
# | | |--base.html
# | | |--index.html
# | |--authapp
# | |--base.html
# | |--index.html

import os
import shutil

temp_dict = 'C://my_project/templates'
if not os.path.exists(temp_dict):
    os.mkdir(temp_dict)

for root, dir, files in os.walk('C://my_project'):
    for file in files:
        if '.html' in file:
            if not 'copy' in file:
                if not os.path.exists(f'{temp_dict}/{os.path.split(root)[1]}'):
                    os.mkdir(f'{temp_dict}/{os.path.split(root)[1]}')
                # можно убрать if not 'copy' in file и в строке ниже "copy_", чтобы файл был с тем же названием.
                # При этом программа выводит ошибку raise SameFileError, но файлы корректно копируются.
                # Такая ошибка предусмотрена самой функцией shutil.copyfile, не очень понятно зачем
                shutil.copyfile(f'{root}/{file}', f'{temp_dict}/{os.path.split(root)[1]}/copy_{file}')

