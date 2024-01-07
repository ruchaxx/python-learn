num1 = input("Enter first number ")
num2 = input("Enter second number ")
num3 = input("Enter third number ")

if int(num1) > int(num2) and int(num1) > int(num3):
    print("{} is max".format(num1))
elif int(num2) > int(num1) and int(num2) > int(num3):
    print("{} is max".format(num2))
else:
    print("{} is max".format(num3))