num = input("Enter a number ")

result = 1
i = 1
while i <= int(num):
    result = i * result
    i = i + 1

print("factorial is ",result)