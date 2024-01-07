num = input("Enter a number ")

print("num ",num)
num_list = list(num)
sum = 0

print("num_list ",num_list)

for j in num_list:
    sum = sum + int(j) ** 3

print("sum ",sum)

if sum == int(num):
    print("{} is Armstrong".format(num))
else:
    print("{} is not Armstrong".format(num))