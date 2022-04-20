import os

folder = 'C:\some_data'

list_100 = [os.path.split(file)[1] for file in os.scandir(folder) if file.stat().st_size <= 100]
list_1000 = [os.path.split(file)[1] for file in os.scandir(folder) if file.stat().st_size <= 1000
             and file.stat().st_size > 100]
list_10000 = [os.path.split(file)[1] for file in os.scandir(folder) if file.stat().st_size <= 10000
              and file.stat().st_size > 1000]
list_100000 = [os.path.split(file)[1] for file in os.scandir(folder) if file.stat().st_size <= 100000
               and file.stat().st_size > 10000]

file_stats_dict = {}

file_stats_dict.setdefault(100, len(list_100))
file_stats_dict.setdefault(1000, len(list_1000))
file_stats_dict.setdefault(10000, len(list_10000))
file_stats_dict.setdefault(100000, len(list_100000))

print(file_stats_dict)