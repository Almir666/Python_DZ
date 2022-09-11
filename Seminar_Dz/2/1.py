# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.

# Пример:
# - 6782 -> 23
# - 0,56 -> 11

from curses.ascii import isdigit


num = input()
result = 0
ls = (i for i in num if i.isdigit())

print(sum(int(i) for i in ls))






# num = float(input())
# result = 0

# while num > 0:
#     result = result + num % 10
#     num = num // 10

# print(int(result))