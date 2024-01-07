num = input("Enter a number ")
i = [2,3,5,7]

# for i in [2,3,5,7]:
#     if int(num) % i == 0 and int(num) != i:
#         print("{} is not prime".format(num))
#         break
#     elif int(num) % i == 0 and int(num) == i:
#         print("{} is  prime".format(num))




if int(num) % 2 == 0 and int(num) != 2:
    print("{} is not prime".format(num))
elif int(num) % 3 == 0 and int(num) != 3:
    print("{} is not prime".format(num))
elif int(num) % 5 == 0 and int(num) != 5:
    print("{} is not prime".format(num))
elif int(num) % 7 == 0 and int(num) != 7:
    print("{} is not prime".format(num))
else:
    print("{} is prime".format(num))
