# Вычислить число c заданной точностью d
# Пример:
# - при $d = 0.001, π = 3.141.$    $10^{-1} ≤ d ≤10^{-10}$

import math

d = input('Задайте d: ')
p = float(input('Задайте число для вычисления: '))
countL = 0
countR = 0
for i in str(d):
    if i != '.':
        countL += 1
    else:
        break    
for i in str(d):
    countR += 1
T = countR - countL - 1

print(round(p, T))

 





