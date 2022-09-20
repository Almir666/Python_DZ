# Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.


# N = int(input('Здадайте число '))

# def Mnoj(n):
#     result = list()
#     d = 2
#     while d <= n:
#         if n % d == 0:
#             result.append(d)
#             n = n/d
#         else:
#             d += 1
#     return result

# print(Mnoj(N))


# N = int(input('Введите число: '))
# list1 = []
# for i in range(2, N+1):
#     if N % i == 0:
#         count = 1
#         for j in range(2, (i//2+1)):
#             if i % j == 0:
#                 count = 0
#         if (count ==1):
#             list1.append(i)
# print(list1)


n = int(input("Введите число N: "))
i = 2 
list = []

while i <= n:
    if n % i == 0:
        list.append(i)
        n //= i
        i = 2
    else:
        i += 1
print(f"Простые множители введенного числа указаны в списке: {list}")