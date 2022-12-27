# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
# Пример:
# для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21] Негафибоначчи

k = int(input('Input number: '))
fib_list = [0, 1]

for i in range(2,k+1):
    fib_list.append(fib_list[i-1] + fib_list[i-2])

nefib_list = fib_list.copy()                                                       # я понимаю что это лютая хренатень, но лучше уже не придумаю

for i in range(0, len(nefib_list), 2):
    nefib_list[i] *= -1

nefib_list.reverse()

res = nefib_list + fib_list
res.remove(0)
print(res)

