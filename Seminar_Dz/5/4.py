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
            count = count + 1
            i += 1
        encoding += str(count) + s[i]
        i += 1
    return encoding

with open('encode.txt', 'r') as data:
    decoding = data.read()

def decode(ss:str):
    count = ''
    str_decode = ''
    for char in ss:
        if char.isdigit():
            count += char 
        else:
            str_decode += char * int(count)
            count = ''
    return str_decode

with open('decode.txt', 'w') as data:
    data.write(decode(decoding))
with open('encode.txt', 'w') as data:
    data.write(encode(s))

print(decode(decoding))

print(encode(s))
