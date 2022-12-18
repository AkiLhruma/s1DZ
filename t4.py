# Напишите программу, которая по заданному номеру четверти, показывает диапазон возможных координат точек в этой четверти (x и y).

while True:
    q = int(input('Input quarter: '))
    if q < 1 or q > 4:
        print('incorrect input')
    else:
        break

if q == 1:
    print('x > 0, y > 0')
elif q == 2:
    print('x < 0, y > 0')
elif q == 3:
    print('x < 0, y < 0')
elif q == 4:
    print('x > 0, y < 0')
