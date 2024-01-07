#map function
def square(num):
    return num**2

nums = [2,3,4]

for i in map(square,nums):
    print(i)

l1 = list(map(square,nums))
print(l1)

#filter function
def even(num):
    return num % 2 == 0

l1 = [1,2,3,4,5,6]
l2 = list(filter(even,l1))
print(l2)

#lambda expression
sqaure_num = lambda num : num ** 2
print(sqaure_num(5))