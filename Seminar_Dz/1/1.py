# Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот день выходным.

# Пример:
# - 6 -> да
# - 7 -> да
# - 1 -> нет

print('Введите цифру от 1 до 7: ')
day = int(input())
if day == 1 or day == 2 or day == 3 or day == 4 or day == 5:
    print('будний')
elif day == 6 or day == 7:
    print('выходной')
else:
    print('вы ввели некорректное число')

        