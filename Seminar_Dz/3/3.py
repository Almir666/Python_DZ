# Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным 
# и минимальным значением дробной части элементов.

# Пример:
# - [1.1, 1.2, 3.1, 5, 10.01] => 0.19

list = [1.1, 1.2, 3.1, 5.0, 10.01]
def MaxEl(list):
    max = round(list[0] % 1, 2)
    for i in list:
        if i % 1 > max:
            max = i % 1
            max = round(max, 2)
    return max

def MinEl(list):
    min = round(list[0] % 1, 2)
    for i in list:
        if i % 1 < min:
            min = i % 1
            min = round(min, 2)
    return min        

result = MaxEl(list) - MinEl(list)

print(result)

