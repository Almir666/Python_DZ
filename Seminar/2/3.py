# 1. Напишите программу, которая принимает на вход число N и выдаёт последовательность из N членов.
# Пример:
# Для N = 5: 1, -3, 9, -27, 81



N = int(input())
j = 1
print(j, end =', ')
for i in range(N -1):
    j = j * -3
    print(j, end =', ')