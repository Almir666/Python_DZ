flag = True
for x in range(0,2):
    for y in range(0,2):
        for z in range(0,2):

            print(not(x | y | z))
            print((not x) & (not y) & (not z))

    if (not(x | y | z)) != ((not x) & (not y) & (not z)):
        flag = False
        break
if flag:
    print('Утверждение истино для всех значений x y z')      
else:
    print('Утверждение ложно')      
           