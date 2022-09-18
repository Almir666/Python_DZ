# Даны два файла, в каждом из которых находится запись многочлена. 
# Задача - сформировать файл, содержащий сумму многочленов.

m1 = '(2 * (x ** 2)) + (4 * x) + 5)'
m2 = '(5 + (x ** 2))'

data = open('m1.txt', 'w')
data.writelines(m1)
data.close()

data = open('m2.txt', 'w')
data.writelines(m2)
data.close()
