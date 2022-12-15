# Напишите программу, которая принимает на вход координаты точки (X и Y), причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости, в 
# которой находится эта точка (или на какой оси она находится).

while True:
    print('Input X coordinate: ', end="")
    x = float(input())

    if x == 0:
        print('incorrect input')
    else:
        break

while True:
    print('Input Y coordinate: ', end="")
    y = float(input())
    if y == 0:
        print('incorrect input')
    else:
        break

print()
if x > 0 and y > 0:
    print(1)
elif x < 0 and y > 0:
    print(2)
elif x < 0 and y < 0:
    print(3)
elif x > 0 and y < 0:
    print(4)