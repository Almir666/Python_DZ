# Вычислить число c заданной точностью d
# Пример:
# - при $d = 0.001, π = 3.141.$    $10^{-1} ≤ d ≤10^{-10}$

# import math

# d = input('Задайте d: ')
# p = float(input('Задайте число для вычисления: '))
# countL = 0
# countR = 0
# for i in str(d):
#     if i != '.':
#         countL += 1
#     else:
#         break    
# for i in str(d):
#     countR += 1
# T = countR - countL - 1

# print(round(p, T))

 
import math
d = input('Введите число d указывающее степень округления числа pi ')
d = d[2:len(d)]
print(round(math.pi,len(d)))

# a = int(input('введите нужную точность 1#= '))
# pi_target = 0
# for i in range(1, 1000000):
#     pi_target += 4 * ((-1) ** (i + 1)) / (2 * i - 1)
# print(str(pi_target)[:a + 2])





