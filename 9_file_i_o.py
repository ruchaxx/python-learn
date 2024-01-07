file = open('test.txt')
print("first time ",file.read())
file.seek(0) #curser 1 line per lai jaay (aa nai lakhiye to biji vaar read karia tyare kai print nai thai)
print("second time ",file.read())
file.seek(0)
print("liness",file.readline())


with open('test.txt') as test_file:
    content = test_file.read()

print(content)


#read
with open('test2.txt',mode='r') as f:
    print("2nd file",f.read())

#append
with open('test2.txt',mode='a') as f:
    f.write("\nfour on fourth")

with open('test2.txt',mode='r') as f:
    print("2nd file",f.read())

with open('test3.txt',mode='w') as f:
    f.write("I created this file")