# Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.

# Пример:
# - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12


list = [2, 3, 5, 9, 3]
sum = 0
j = 1
for i in range(0,len(list) - 1):
    if j % 2 != 0:
        sum = sum + list[j]
        j += 1
    else:
        j +=1   
print(sum)



