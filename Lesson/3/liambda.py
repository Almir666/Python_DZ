
# list = [(i, i**2) for i in (1,2,3,5,8,15,23,38) if i % 2 == 0]
# print(list)


def where(f, col):
    return [x for x in col if f(x)]

def select(f, col):
    return [f(x) for x in col]

data = '1 2 3 5 8 15 23 38'.split()

res = select(int, data)
res = where(lambda x: not x%2, res)
res = select(lambda x: (x, x**2), res)
print(res)



