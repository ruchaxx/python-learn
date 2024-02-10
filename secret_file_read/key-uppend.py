import yaml
import sys

file_name = sys.argv[1]

with open(file_name,mode='r') as f:
    file = list(yaml.safe_load_all(f))

#print("file ",file[0])
    
l1 = []

for i,j in file[0].items():
   # print("key ",i)
   # print("value ",j)
    if i == 'data':
        for key,value in j.items():
            l1.append(key)

#print("list ",l1)

with open("value.txt",mode='r') as f:
    l2 = f.read()

#print("l2 ",type(l2))

l3 = []
l3.append(l2)

#print("l3 ",l3)

d1 = {}

for i in l1:
         for j in l3:
              d1[i] = j

#print("d1 ",d1)

with open("key.txt",mode='w') as f:
    for i in l1:
            f.write(i+": ")
            f.write("\n")

    # for j in l3:
    #      f.write(j)

    # for i in l1:
    #      for j in l3:
    #           f.write(i+": "+j)
    #           break
    #      break



