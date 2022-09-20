# Создайте программу для игры с конфетами человек против человека.
# Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга.
# Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет.
# Все конфеты оппонента достаются сделавшему последний ход. Сколько конфет нужно взять первому игроку,
# чтобы забрать все конфеты у своего конкурента?

# a) Добавьте игру против бота
# b) Подумайте как наделить бота ""интеллектом""

import random
game = input('Выеберите с кем играть, с ботом или с игроком, просто напишите: бот/игрок ')
flag = False
if game == 'бот': 
    flag = True

    Candys = int(input('Введите колличество конфет: '))
    name = input('Введите имя игрока: ')
    first = random.randint(0, 1)
    listName = []
    if first == 0:
       listName.append(name)
       listName.append('bot')
       print('Первым ходит:', name)
    else:
       listName.append(name)
       listName.append('bot')
       print('Первым ходит:', 'bot')
    taken = 0
    j = first
    i = first

    run = True
    def bot(start):
           if start == True:
               stepBot = random.randint(1, 28)
           return stepBot
    change = False       
    if first == 1:
        change = True
    while Candys > 0:
        if change == True:
            print('Ход ботa')   
            if Candys % 29 != 0:
                    prep = Candys % 29
                    r = prep
            else:
                    r = bot(run)
            Ost = Candys - r
            Candys = Ost
            count = taken + r
            taken = count
            if i == 0:
                    i += 1
            else:
                    i -= 1   
            if Ost <= 0:
                if i == 0:
                    i += 1
                else:
                    i -= 1 
                print(f'Конец игры, {listName[i]} забрал все конфеты и победил')
                break                
            print('Конфет на столе осталось: ', Ost)
            print('Конфет у bot: ', count)
            print(f'Теперь вы {name}')
            change = False
        else:
            step = int(input())
            if step < 1 or step > 28:
                print('Можно взять от 1 до 28 конфет строго! Придется начать игру заново')
                break
            Ost = Candys - step
            Candys = Ost
            count = taken + step
            taken = count
            if i == 0:
                    i += 1
            else:
                    i -= 1      
            if Ost <= 0:
                if i == 0:
                    i += 1
                else:
                    i -= 1 
                print(f'Конец игры, {listName[i]} забрал все конфеты и победил')
                break         
            print('Конфет на столе осталось: ', Ost)
            print(f'Конфет у {name}: ', count)
            print(f'Теперь ходит бот')
            change = True

else:
    if game == 'игрок':

        Candys = int(input('Введите колличество конфет: '))
        name1 = input('Введите имя первого игрока: ')
        name2 = input('Введите имя второго игрока: ')
        first = random.randint(0, 1)
        listName = []
        if first == 0:
            listName.append(name1)
            listName.append(name2)
            print(name1, ' выйграл жребий и ходит первым')
        else:
            listName.append(name1)
            listName.append(name2)
            print(name2, ' выйграл жребий и ходит первым')
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

                    if i == 0:
                        i += 1
                    else:
                        i -= 1
                    if Ost <= 0:
                        print(f'Конец игры, {listName[j]} забрал все конфеты и победил')
                        break
                    print('Конфет на столе осталось: ', Ost)
                    print(f'Конфет у {listName[j]}: ', count)
                    print(f'Теперь вы {listName[i]}')
                    if j == 0:
                        j += 1
                    else:
                        j -= 1
    else:
        print('Можно ввести только слово бот или игрок, без дургих специальных символов или цифр')                    
                     
