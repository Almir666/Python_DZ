# Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.


N = int(input('Здадайте число '))

def Mnoj(n):
    result = list()
    d = 2
    while d <= n:
        if n % d == 0:
            result.append(d)
            n = n/d
        else:
            d += 1
    return result

print(Mnoj(N))
