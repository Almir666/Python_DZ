# Напишите программу, которая по заданному номеру четверти, показывает
# диапазон возможных координат точек в этой четверти (x и y).

print('Введите номер координаты')
N = int(input())
if N == 1:
    print('x(0; бесконечность) y(0; бесконеность)')
elif N == 2:
    print('x(-бесконечность; 0) y(0; бесконеность)')
elif N == 3:
    print('x(-бесконечность; 0) y(-бесконеность; 0)')
elif N == 4:
    print('x(0; бесконечность) y(-бесконеность; 0)')
else:
    print('Введите число от 1 до 4')    
