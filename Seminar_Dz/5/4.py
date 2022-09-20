# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.

path = 'Dz_5_input.txt'
with open(path) as file:
    s = file.readline()

def encode(s):
    encoding = "" 
    i = 0
    while i < len(s):
        count = 1
        while i + 1 < len(s) and s[i] == s[i + 1]:
            count += 1
            i += 1
        encoding += str(count) + s[i]
        i += 1
    return encoding

with open('encode.txt', 'w') as data:
    data.write(encode(s))    

with open('encode.txt', 'r') as data:
    decoding = data.read()

def decode(ss:str):
    number = ''
    words = ''
    for i in ss:
        if i.isdigit():
            number += i 
        else:
            words += i * int(number)
            number = ''
    return words

with open('decode.txt', 'w') as data:
    data.write(decode(decoding))

print(encode(s))
print(decode(decoding))

