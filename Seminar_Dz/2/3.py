# Задайте список из N элементов, заполненных числами из промежутка [-N, N]. Найдите произведение
#  элементов на указанных позициях. Позиции хранятся в файле file.txt в одной строке одно число.


print('Введите число N: ')
N = int(input())
for i in range(-N, N + 1):
    list = [] + [i]
print(list)
   