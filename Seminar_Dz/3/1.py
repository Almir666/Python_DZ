# Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.

# Пример:
# - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12


# list = [2, 3, 5, 9, 3]
# sum = 0
# j = 1
# for i in range(0,len(list) - 1):
#     if j % 2 != 0:
#         sum = sum + list[j]
#         j += 1
#     else:
#         j +=1   
# print(sum)


a = int(input('Введите кол-во чисел в списке for 1# = '))
list_a = list((i-i+1)*randint(0, 10) for i in range(a))
print(list_a)
sum_a = sum(list_a[i] for i in range(1, a, 2))
print(sum_a)

# list1 = [2, 3, 5, 9, 3]
# sum = 0
# for i in range(len(list1)):
#     if i %2 != 0:
#         sum += list1[i]
# print(sum)

# list = [2, 3, 5, 9, 3]
# print(sum(list[1:5:2]))


# list1=[int(input()) for _ in range(int(input()))] 
# summ=0
# for i in range (1, len(list1), 2):
#     summ+=list1[i]
# print(summ)

