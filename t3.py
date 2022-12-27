# Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов, отличной от 0.
# Пример:
# [1.1, 1.2, 3.1, 5, 10.01] => 0.19

import random

#my_list = [1.1, 1.2, 3.1, 5, 10.01]

my_list = []
for i in range(random.randrange(5,10)):
    my_list.append(round(random.uniform(1, 10), 2))
print(my_list)

for i in my_list:
    if i - int(i) != 0:
        min = i
        max = i
        break

for i in my_list:
    if i - int(i) != 0:
        if min % 1 > i % 1:
            min = i
        if max % 1 < i % 1:
            max = i

res = max % 1 - min % 1
print(f'max = {max}, min = {min}, res = {round(res, 2)}')
