num = input("Enter a number ")
if num == num[::-1]:
    print("{} is palindrome".format(num))
else:
    print("{} is not palindrome".format(num))