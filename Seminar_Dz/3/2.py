# Напишите программу, которая найдёт произведение пар чисел списка. 
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.

# Пример:
# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]

list = [2, 3, 4, 5, 6]
i = 0
m = 1
while i < ((len(list) / 2)):
    result = list[i] * list[(len(list) - m)]
    print(result,end=' ')
    i += 1
    m += 1



