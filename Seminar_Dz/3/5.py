# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.

# Пример:
# - для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]

N = int(input('Введите число '))
list = []
list.append(0)
list.append(1)
list.insert(0, -1)
def Fibonachi(n):
    index = -1
    for i in range(2, n + 1):
        list.append(list[i * 2 - 2] + list[i * 2 - 3])
        list.insert(0, (abs(list[0]) + abs(list[1])) * index)
        index = index * -1
    print(list)
Fibonachi(N)        






   


