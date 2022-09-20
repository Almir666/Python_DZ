# # Создайте программу для игры в ""Крестики-нолики""


# field = [['_','_','_'], ['_','_','_'], ['_','_','_']]

# def printfield(array):
#     for i in array:
#         for j in i:
#             print(j,end=" ")
#         print()
# printfield (field)

Candies = int(input())
win = Candies % 29
print(round(win))


