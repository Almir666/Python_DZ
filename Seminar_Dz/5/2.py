# Создайте программу для игры с конфетами человек против человека.
# Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга.
# Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет.
# Все конфеты оппонента достаются сделавшему последний ход. Сколько конфет нужно взять первому игроку,
# чтобы забрать все конфеты у своего конкурента?

# a) Добавьте игру против бота
# b) Подумайте как наделить бота ""интеллектом""

import random
name1 = input('Введите имя первого игрока: ')
name2 = input('Введите имя второго игрока: ')
first = random.randint(0, 1)
listName = []
if first == 0:
    listName.append(name1)
    listName.append(name2)
    print('Первым ходит:', name1)
else:
    listName.append(name2)
    listName.append(name1)
    print('Первым ходит:', name2)
Candys = 221
taken = 0
j = first
i = first
print('Введите число от 1 до 28')
if Candys != 0:
    while Candys > 0:
        step = int(input())
        if step < 1 or step > 28:
            print('Можно взять от 1 до 28 конфет строго! Придется начать игру заново')
            break
        else:     
            Ost = Candys - step
            Candys = Ost
            count = taken + step
            taken = count
            if j == 0:
                j +=1
            else:
                j -=1   
            if Ost <= 0:
                print(f'Конец игры, победил {listName[j]}')
            print('Конфет на столе осталось: ',Ost)
            print(f'Конфет у {listName[j]}: ', count)  
            print(f'Теперь вы {listName[i]}')
            if i == 0:
                i +=1
            else:
                i -=1   
      
