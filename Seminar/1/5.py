# Напишите программу которая принимает на вход число и проверяет 
# кратно ли оно 5, 10, 15 но не 30


print('Введите число N: ')
N = int(input())
if (N % 5 == 0 and N % 10 == 0 or N % 15 == 0) and N % 30 != 0:
    print('кратно')
else:
    print('не кратно')    
       