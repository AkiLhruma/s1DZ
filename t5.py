# Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве.
# Пример:
# - A (3,6); B (2,1) -> 5,09
# - A (7,-5); B (1,-1) -> 7,21

print('Input x1 coordinate: ', end="")
x1 = float(input())
print('Input x1 coordinate: ', end="")
y1 = float(input())
print('Input x1 coordinate: ', end="")
x2 = float(input())
print('Input x1 coordinate: ', end="")
y2 = float(input())

d = round(pow((x1 - x2)**2 + (y1 - y2)**2, 0.5), 2)
print(d)