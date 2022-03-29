#  2. Создать список, состоящий из кубов нечётных чисел от 1 до 1000 (куб X - третья степень числа X):

cube_list = []
for i in range(1, 1000):
    if i % 2 != 0:
        cube_list.append(i ** 3)

# a. Вычислить сумму тех чисел из этого списка, сумма цифр которых делится нацело на 7.
# Например, число «19 ^ 3 = 6859» будем включать в сумму, так как 6 + 8 + 5 + 9 = 28 –
# делится нацело на 7. Внимание: использовать только арифметические операции!

sum_list_7 = []
for i in cube_list:
    numbers = [int(i) for i in str(i)]
    sum = 0
    for x in numbers:
        sum += x
    if sum % 7 == 0:
        sum_list_7.append(i)
print(sum_list_7)

# b. К каждому элементу списка добавить 17 и заново вычислить сумму тех чисел из этого
# списка, сумма цифр которых делится нацело на 7

new_cube_list = []
for x in cube_list:
    new_cube_list.append(x + 17)
print(new_cube_list)

sum_list_7 = []
for i in new_cube_list:
    numbers = [int(i) for i in str(i)]
    sum = 0
    for x in numbers:
        sum += x
    if sum % 7 == 0:
        sum_list_7.append(i)
print(sum_list_7)
