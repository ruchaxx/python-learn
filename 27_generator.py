def cube_num(n):
    for x in range(n):
        yield x**3


for x in cube_num(10):
    print(x)
