l = [1,2,3,4,5,6,7,8,9,10]
for i in l:
    print(i)

for i in l:
    #check even num
    if i % 2 == 0:
        print("even num",i)
    else:
        print("odd num",i)


sum = 0
for i in l:
    sum = sum + i

print("sum ",sum)

s = "hello world"

for letter in s:
    print(letter)

for _ in s:
    print("cool")

#tupple unpacking
lis = [(1,2),(4,5),(6,7)]
for (a,b) in lis:
    print(a)
    print(b)

#iterate dict
d = {'k1': 1, 'k2' : 2, 'k3' : 3}

for i in d.items():
    print(i)

for key,value in d.items():
    print(key)
    print(value)

#pass
l = [1,2,3,4,5,6,7,8,9,10]
for i in l:
    pass

#continue
s = "rucha"
for i in s:
    if i == 'u':
        continue
    else:
        print("continue",i)

#break
s = "rucha"
for i in s:
    if i == 'c':
        break
    else:
        print("break",i)