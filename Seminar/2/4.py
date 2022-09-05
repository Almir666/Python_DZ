# Напишите программу, в которой пользователь будет задавать две строки, 
# а программа - определять количество вхождений одной строки в другой.

string_1 = input()
string_2 = input()
if string_1 > string_2:
    print(string_1.count(string_2))
else:
    print(string_2.count(string_1))