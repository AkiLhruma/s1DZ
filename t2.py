# Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# Пример:
# [2, 3, 4, 5, 6] => [12, 15, 16];
# [2, 3, 5, 6] => [12, 15]

import random

my_list = []
for i in range(random.randrange(5,10)):
    my_list.append(random.randint(1, 10))

i1 = 0
i2 = -1
length = len(my_list) - 1
comp_list = []

if length % 2 == 0:
   length += 1

while i1 < length / 2:
    comp_list.append(my_list[i1] * my_list[i2])
    i1 += 1
    i2 -= 1
print(f'{my_list} => {comp_list}')