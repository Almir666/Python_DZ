# Напишите программу, которая найдёт произведение пар чисел списка. 
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.

# Пример:
# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]

# list = [2, 3, 4, 5, 6]
# i = 0
# m = 1
# while i < ((len(list) / 2)):
#     result = list[i] * list[(len(list) - m)]
#     print(result,end=' ')
#     i += 1
#     m += 1

# list1 = [2, 3, 4, 5, 6]
# n = len(list1)
# list2 = []
# k=int(len(list1)/2+len(list1)%2)
# len(list2)==k
# for i in range(k):
#     list2.append((list1[i]*list1[n-1-i]))
# print(list2)

my_list = [2, 3, 4, 5, 6]
result_list = []
for i in range((len(my_list)+1)//2):
    result_list.append(my_list[i] * my_list[len(my_list)-1-i])
print(result_list)

import random

b = int(input('Введите кол-во чисел в списке for 2# = '))
list_b = list(random.randint(0, 10) for i in range(b))
print(list_b)
proiz_b = list(list_b[i]*list_b[-1*(1+i)] for i in range(b//2+1*(b%2)))
print(proiz_b)