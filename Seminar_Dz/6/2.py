# Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, 
# стоящих на нечётной позиции.

# Пример:
# - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12


list_input = [2,3,5,9,3]

# def find(ls):
#     el =[]
#     for i in range(len(ls)):
#         if i % 2:
#             el.append(ls[i])
#     return sum(el)   

# print(find(list_input))

res = filter(lambda x: x not in list_input[x % 2 == 0], list_input)
print(int(res))