#range
for num in range(10):
    print(num)

for num in range(3,10):
    print(num)

l = list(range(0,11,2))
print(l)

####
index_count = 0
for i in 'abcde':
    print("at index {} the i is {}".format(index_count,i))
    index_count += 1

#enumerate
word = 'abcde'
for i in enumerate(word):
    print("enumerate ",i)


#zip
l1 = [1,2,3,4,5,6]
l2 = ['a','b','c']
l3 = [100,200,300]
for i in zip(l1,l2,l3):
    print("zip ",i)

#in
2 in [1,2,3]

'a' in 'a world'

d = {'k1' : 43}
43 in d.values()

#min/max

l1 = [2,3,4,5,6]
min(l1)
max(l1)

#random lib
##shuffle
from random import shuffle

l1 = [1,2,3,4,5,6,7]
shuffle(l1)
print("shuffle",l1)

##randint
from random import randint
num = randint(0,100)
print("random int",num)

#input from user
result = input('your name: ')
print(result)