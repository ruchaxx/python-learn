import yaml
import os,glob
import sys

operation = sys.argv[1]

filelist = []

def add_key(l1,request_memory,limit_memory,request_cpu,limit_cpu):
    if request_memory == False:
        l1.append({'name': 'resources.requests.memory', 'value': ''})
    if limit_memory == False:
        l1.append({'name': 'resources.limits.memory', 'value': ''})
    if request_cpu == False:
        l1.append({'name': 'resources.requests.cpu', 'value': ''})
    if limit_cpu == False:
        l1.append({'name': 'resources.limits.cpu', 'value': ''})

def delete_key(l1):
    for i in range(len(l1)):
        if l1[i]['name'] == "resources.requests.memory":
            del l1[i]
            break

    for i in range(len(l1)):
        if l1[i]['name'] == "resources.limits.memory":
            del l1[i]
            break

    for i in range(len(l1)):
        if l1[i]['name'] == "resources.requests.cpu":
            del l1[i]
            break

    for i in range(len(l1)):
        if l1[i]['name'] == "resources.limits.cpu":
            del l1[i]
            break

for filename in glob.glob('argocd/*/aws/non-prod-2/*.yaml'):
    filelist.append(filename)

for filepath in filelist:
    with open(filepath,mode='r') as f:
        data = yaml.safe_load(f)


    l1 = data['spec']['source']['helm']['parameters']


    request_memory = False
    request_cpu = False
    limit_memory = False
    limit_cpu = False

    for i in l1:
        if "resources.requests.memory"  in str(i):
            request_memory = True
        if "resources.limits.memory"  in str(i):
            limit_memory =  True
        if "resources.requests.cpu"  in str(i):
            request_cpu = True
        if "resources.limits.cpu"  in str(i):
            limit_cpu = True

    if operation == "add":
        add_key(l1,request_memory,limit_memory,request_cpu,limit_cpu)
    if operation == "delete":
        delete_key(l1)



    for key,value in data.items():
        if key == "spec":
            data['spec']['source']['helm']['parameters'] = l1
        else:
            pass


    with open(filepath,mode='w') as f:
        f.write(yaml.safe_dump(data))


print("done")



