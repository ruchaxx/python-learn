import yaml
import os,glob
import re

with open("accs-fdn-svc/values.yaml",mode='r') as file:
    valuesFileData = list(yaml.safe_load_all(file))

var_list = []

for elmt in valuesFileData:
    for key,value in elmt.items():
        var_list.append(key)

print("\nvar_list ",var_list)

value_list = []

for filename in glob.glob('accs-fdn-svc/templates/*.*'): #config ,deployment
    with open(os.path.join(os.getcwd(), filename), 'r') as f:
        data = f.read()

    with open("test.txt",mode='w') as file:
        file.write(data)

    with open("test.txt",mode='r') as file:
        for line in file:
            if '.Values.' in line:
                value_list.append((line.strip().split('.Values.'))[1])

final_list = []
final_set = set()

for i in value_list:
    final_set.add(i.split(" ")[0].split(".")[0])

print("\nfinal set ",final_set)

for i in final_set:
    final_list.append(i)



print("\nfinal list ",final_list)

missing_list = []

is_present = False

for var in final_list:
    for param in var_list:
        if var == param:
            is_present = True
            break
        else:
            is_present = False

    if is_present == False:
        missing_list.append(var)


if not missing_list:
    print("\nAll variables are present in values.yaml ")
else:
    print("\nThese variables are missing in values.yaml ",missing_list)




