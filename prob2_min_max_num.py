num1 = input("Enter first number ")
num2 = input("Enter second number ")
if int(num1) > int(num2):
    print("{} is max".format(num1))
    print("{} is min".format(num2))
else:
    print("{} is max".format(num2))
    print("{} is min".format(num1))