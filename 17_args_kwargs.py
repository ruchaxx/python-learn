def func(a,b):

    return sum ((a,b)) * 0.05  # 5% of sum

result = func(40,60)
print(result)

#*args
def func(*args):

    return sum (args) * 0.05  # args ni jagya e kai pan use thai e.g num

result = func(40,60,80)  #tupple store thai
print(result)

#*kwargs
def myfunc(**kwargs):
    if 'fruit' in kwargs:
        print("fruit is {}".format(kwargs['fruit']))
    else:
        print("no fruit")

result = myfunc(fruit = 'apple') #dict store thai
print(result)
