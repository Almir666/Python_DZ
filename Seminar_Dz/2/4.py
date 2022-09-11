# Реализуйте алгоритм перемешивания списка.

import random
list = [1, 2, 3, 4, 5, 6, 7]
t = 0
while t < len(list):
    r = random.randint(0,len(list) - 1)
    j = 1
    swap = list[r]
    list[r] = list[len(list) - j]
    list[len(list) - j] = swap
    j += 1
    t += 1
print(list)    

