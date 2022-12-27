# Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на позиции с нечетным индексом.
# Пример:
# [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12
import random

array = []
for i in range(random.randrange(5,10)):
    array.append(random.randint(1, 10))
print(array)
uneven = []
sum = 0
for i in range(1, len(array), 2):
    uneven.append(array[i])
    sum += array[i]

print(f'На нечетных позициях элементы {uneven}, ответ: {sum}')