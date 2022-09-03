# Напишите программу которая на вход принимает 5 чисел и находит максимальное из них

# print('Введите пять чисел через пробел:')
# num = [int(i) for i in input().split()]
# print(num)
# max = num[0]
# for i in range(len(num)):
#     if num[i] > max:
#         max = num[i]

# print(max)
print('Введите пять чисел через пробел:')
num = [int(i) for i in input().split()[:5]]
print(num)
print(max(num))