# Напишите программу, которая принимает на вход координаты точки (X и Y), причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости, в которой находится эта точка (или на какой оси она находится).

# Пример:
# - x=34; y=-30 -> 4
# - x=2; y=4-> 1
# - x=-34; y=-30 -> 3

print('Введите координаты X и Y')
x = int(input())
y = int(input())
if x > 0 and y > 0:
    print('первая плоскоть')
elif x < 0 and y > 0:
    print('вторая плоскоть')
elif x < 0 and y < 0: 
    print('третья плоскоть')
elif x > 0 and y < 0:
    print('четвертая плоскоть')
else:
    print('координата не принадлежит никакой плоскости')    