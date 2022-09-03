# Напишите программу которая на вход принимает 5 чисел и находит максимальное из них

# num = [int(i) for i in input().split()]
# print(num)
# max = num[0]
# for i in range(len(num)):
#     if num[i] > max:
#         max = num[i]

# print(max)

num = [int(i) for i in input().split()]
print(num)
print(max(num))