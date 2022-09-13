# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.

# Пример:
# - 6782 -> 23
# - 0,56 -> 11

# from curses.ascii import isdigit


# num = input()
# result = 0
# ls = (i for i in num if i.isdigit())

# print(sum(int(i) for i in ls))

# numb = float(input())
# summ = 0
# for el in str(numb):
#     if el != '.':
#         summ += int(el)
# print(summ)

n = float(input('Введите число: '))
while n % 1 > 0:
    n *= 10
summ = 0
while n > 0:
    summ += n % 10
    n //= 10
print(int(summ))






# num = float(input())
# result = 0

# while num > 0:
#     result = result + num % 10
#     num = num // 10

# print(int(result))