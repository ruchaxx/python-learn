import yaml
import os,glob
import sys
import subprocess

operation = sys.argv[1]
password = sys.argv[2]

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

########################################################################
print("starting..................")

dirlist = []
dirlist = os.listdir("argocd")

print("dirlist ",dirlist)

chartdir = {}

for i in dirlist:
    chartdir[i] = ''

#print("chartdir ",chartdir)

for filename in glob.glob('argocd/*/aws/non-prod-2/*.yaml'):
    filelist.append(filename)

for filepath in filelist:
    with open(filepath,mode='r') as f:
        data = yaml.safe_load(f)

    for chart,version in chartdir.items():
        for key,value in data.items():
            if data['spec']['source']['chart'] == chart:
                chartdir[chart] = data['spec']['source']['targetRevision']
            else:
                pass


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

print("\nupdated chartdir ",chartdir)

os.system('cmd /c "helm registry login ghcr.io/bentlynevada-bh/ --username shyam-ks --password ${{ secrets.GH_TOKEN }}')

for chart,version in chartdir.items():
    print("helm pull oci://ghcr.io/bentlynevada-bh/"+chart +" --version "+ version)
    print("tar -zxvf ./"+chart+"-"+version+".tgz")

print("done")


##################################################################3
def update_value():
    argocddir = os.listdir("argocd")
    helmdir = os.listdir("helm-charts")

    #print("argocddir ",argocddir)
    #print("helmdir ",helmdir)



    for chart  in helmdir:
        for svc in argocddir:
            if chart == svc:

                with open("helm-charts/"+chart+"/values.yaml",mode='r') as f:
                    value_data = yaml.safe_load(f)

                resource = {}

                for key,value in value_data.items():
                    if key == "resources":
                        resource.update(value)


                #print("\nresource ",resource)

                memory_limit = ''
                cpu_limit = ''
                memory_request = ''
                cpu_request = ''

                for key,value in resource.items():
                    if key == "limits":
                        memory_limit = resource['limits']['memory']
                        cpu_limit = resource['limits']['cpu']
                    if key == "requests":
                        memory_request = resource['requests']['memory']
                        cpu_request = resource['requests']['cpu']

                filelistnew = []
                for filename in glob.glob('argocd/'+svc+'/aws/non-prod-2/*.yaml'):
                    filelistnew.append(filename)

                #print("\nfilelistnew ",filelistnew)

                for filepath in filelistnew:
                    with open(filepath,mode='r') as f:
                        data = yaml.safe_load(f)

                    l1 = data['spec']['source']['helm']['parameters']

                    #print("\nbefore l1 ",l1)

                    for i in l1:
                        if "resources.requests.memory"  in str(i):
                            i['value'] = memory_request
                        if "resources.limits.memory"  in str(i):
                            i['value'] = memory_limit
                        if "resources.requests.cpu"  in str(i):
                            i['value'] = cpu_request
                        if "resources.limits.cpu"  in str(i):
                            i['value'] = cpu_limit


                    #print("\nafter l1 ",l1)

                    for key,value in data.items():
                            if key == "spec":
                                data['spec']['source']['helm']['parameters'] = l1
                            else:
                                pass

                    #print("\nlast data ",data)

                    with open(filepath,mode='w') as f:
                        f.write(yaml.safe_dump(data))



update_value()


#os.system('cmd /c "helm registry login ghcr.io/bentlynevada-bh/ --username shyam-ks --password "'+password)
# os.system('cmd /k "helm pull oci://ghcr.io/bentlynevada-bh/accs-fdn-svc --version 1.0.217"')

#subprocess.run(["helm" , "registry","login", "ghcr.io/bentlynevada-bh/"," --username "," shyam-ks ", " --password  ",password])
