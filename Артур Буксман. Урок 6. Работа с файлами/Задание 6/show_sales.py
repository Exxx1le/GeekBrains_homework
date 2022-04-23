import sys

with open('bakery.csv', 'r', encoding='utf-8') as f:
    if len(sys.argv) < 2:
        for i in f:
            print(i)
    elif len(sys.argv) == 2:
        user_input = int(sys.argv[1])
        for i in f.readlines()[:user_input]:
            print(i)
    elif len(sys.argv) == 3:
        user_start = int(sys.argv[1]) - 1
        user_end = int(sys.argv[2])
        for i in f.readlines()[user_start:user_end]:
            print(i)
