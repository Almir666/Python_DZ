# В файле находится N натуральных чисел, записанных через пробел. Среди чисел не хватает одного, чтобы выполнялось 
# условие A[i] - 1 = A[i-1]. Найдите это число.


def find_num(lst):
    for i in range(1, len(lst)):
        if lst[i] - lst[i - 1] > 1:
            return i, lst[i] - 1
    return -1, -1


with open("data.txt", "r") as fin:
    lst = [int(i) for i in fin.readline().split()]
    print(lst)
    pos, num = find_num(lst)
    print(pos,num)
    if (pos != -1):
        lst.insert(pos, num)
    print(lst)

# file = open('file.txt', 'a')
# while True:
#     s = input(' ')
#     if s == "":
#         break
#     file.write(s+"\n")
# file.close()

# for i in range(file):
#     if (file[i - 1] - file[i]) > 1:
#         file.insert(i, file[i] + 1)
#         print(file[i] + 1)


# with open('tex.txt','r') as n:
#     lst = [int(i) for i in n.readline().split()]
#     for i in range(1,len(lst)):
#         if lst[i] - lst[i - 1] > 1:
#             print(lst[i]-1)


