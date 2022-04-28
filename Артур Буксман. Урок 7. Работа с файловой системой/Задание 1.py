# Написать скрипт, создающий стартер (заготовку) для проекта со следующей структурой папок:
# |--my_project
#   |--settings
#   |--mainapp
#   |--adminapp
#   |--authapp
import os


def folders_creation(root_folder, *args):
    if not os.path.exists(root_folder):
        os.mkdir(root_folder)
    for i in args:
        dir_path = os.path.join(root_folder, i)
        os.mkdir(dir_path)


folders_creation('my_project', 'settings', 'mainapp', 'adminapp', 'authapp')
