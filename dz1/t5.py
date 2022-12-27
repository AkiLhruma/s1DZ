# Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве.
# Пример:
# - A (3,6); B (2,1) -> 5,09
# - A (7,-5); B (1,-1) -> 7,21

x1 = float(input('Input x1 coordinate: '))
y1 = float(input('Input y1 coordinate: '))
x2 = float(input('Input x2 coordinate: '))
y2 = float(input('Input y2 coordinate: '))

d = round(pow((x1 - x2)**2 + (y1 - y2)**2, 0.5), 2)
print(d)