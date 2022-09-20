# Задайте последовательность чисел. Напишите программу, которая выведет список 
# неповторяющихся элементов исходной последовательности.


numbers = [1, 2, 3, 3, 4, 4, 4, 5]
list = []
for i in numbers:
   if numbers.count(i) == 1:
       list.append(i)
print(list)       


# def elements(nums):
#     nums = [int(i) for i in nums.split()]
#     return list(set(nums))

# numbers = '1 1 2 2 3 455 66 66 2 1'
# print(elements(numbers))