# Напишите программу, которая будет преобразовывать десятичное число в двоичное.

# Пример:
# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10

N = int(input('Введите число: '))
ost = ''
while N > 0:
    ost = str(N % 2) + ost
    N = N // 2
    
print(ost)








