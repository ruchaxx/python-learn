s1 = 'hello'
l1 = []
for i in s1:
    l1.append(i)

print(l1)

#comprehension
l2 = [i for i in s1]
print("comprehension",l2)

l3 = [x**2 for x in range(0,11)]
print(l3)

l4 = [x for x in range(0,11) if x%2==0]
print(l4)

result = [x if x%2==0 else 'odd' for x in range(0,11)]
print(result)

#nested loop
l1 = []
for x in [2,4,6]:
    for y in [100,200,300]:
        l1.append(x*y)

print("nested loop",l1)

#comprehension for nested loop
l1 = [x*y for x in [2,4,6] for y in [1,10,1000]]
print("comprehension nested loop",l1)
