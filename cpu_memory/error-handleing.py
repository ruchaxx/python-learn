import yaml
import os,glob
import sys
import subprocess

operation = sys.argv[1]
password = sys.argv[2]

filelist = []

def add_key(l1,request_memory,limit_memory,request_cpu,limit_cpu):
    #print("l1 ",l1)
    if request_memory == False:
        l1.append({'name': 'resources.requests.memory', 'value': ''})
    if limit_memory == False:
        l1.append({'name': 'resources.limits.memory', 'value': ''})
    if request_cpu == False:
        l1.append({'name': 'resources.requests.cpu', 'value': ''})
    if limit_cpu == False:
        l1.append({'name': 'resources.limits.cpu', 'value': ''})

def delete_key(l1):
    #sprint("in dlete func")
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

def customkpi_add_key(l1,wrapper_request_memory,wrapper_limit_memory,wrapper_request_cpu,wrapper_limit_cpu,
                      pyexe_request_memory,pyexe_limit_memory,pyexe_request_cpu,
                      pyexe_limit_cpu):
    if wrapper_request_memory == False:
        l1.append({'name': 'customKpiWrapperSvc.resources.requests.memory', 'value': ''})
    if wrapper_limit_memory == False:
        l1.append({'name': 'customKpiWrapperSvc.resources.limits.memory', 'value': ''})
    if wrapper_request_cpu == False:
        l1.append({'name': 'customKpiWrapperSvc.resources.requests.cpu', 'value': ''})
    if wrapper_limit_cpu == False:
        l1.append({'name': 'customKpiWrapperSvc.resources.limits.cpu', 'value': ''})

    if pyexe_request_memory == False:
        l1.append({'name': 'customKpiPyExecSvc.resources.requests.memory', 'value': ''})
    if pyexe_limit_memory == False:
        l1.append({'name': 'customKpiPyExecSvc.resources.limits.memory', 'value': ''})
    if pyexe_request_cpu == False:
        l1.append({'name': 'customKpiPyExecSvc.resources.requests.cpu', 'value': ''})
    if pyexe_limit_cpu == False:
        l1.append({'name': 'customKpiPyExecSvc.resources.limits.cpu', 'value': ''})

def customkpi_delete_key(l1):
    print("in customkpi dlete func")
    for i in range(len(l1)):
        if l1[i]['name'] == "customKpiWrapperSvc.resources.requests.memory":
            del l1[i]
            break

    for i in range(len(l1)):
        if l1[i]['name'] == "customKpiWrapperSvc.resources.limits.memory":
            del l1[i]
            break

    for i in range(len(l1)):
        if l1[i]['name'] == "customKpiWrapperSvc.resources.requests.cpu":
            del l1[i]
            break

    for i in range(len(l1)):
        if l1[i]['name'] == "customKpiWrapperSvc.resources.limits.cpu":
            del l1[i]
            break
    for i in range(len(l1)):
        if l1[i]['name'] == "customKpiPyExecSvc.resources.requests.memory":
            del l1[i]
            break

    for i in range(len(l1)):
        if l1[i]['name'] == "customKpiPyExecSvc.resources.limits.memory":
            del l1[i]
            break

    for i in range(len(l1)):
        if l1[i]['name'] == "customKpiPyExecSvc.resources.requests.cpu":
            del l1[i]
            break

    for i in range(len(l1)):
        if l1[i]['name'] == "customKpiPyExecSvc.resources.limits.cpu":
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

    #print("\ndata ",data)


    if data == None:
        #print("in if")
        pass
    else:
        #print(data.get('apiVersion'))
        pass

    if data == None:
        #print("in iff")
        pass
    else:
        #print("in else....")
        for chart,version in chartdir.items():
            for key,value in data.items():
                if data['spec']['source']['chart'] == chart:
                    chartdir[chart] = data['spec']['source']['targetRevision']
                else:
                    pass

        if data['spec']['source']['chart'] == "custom-kpi-svc":
            print("in cudtm ifff")
            customkpi = data['spec']['source']['helm']['parameters']
            wrapper_request_memory = False
            wrapper_request_cpu = False
            wrapper_limit_memory = False
            wrapper_limit_cpu = False

            pyexe_request_memory = False
            pyexe_request_cpu = False
            pyexe_limit_memory = False
            pyexe_limit_cpu = False


            for i in customkpi:
                if "customKpiWrapperSvc.resources.requests.memory"  in str(i):
                    wrapper_request_memory = True
                if "customKpiWrapperSvc.resources.limits.memory"  in str(i):
                    wrapper_request_cpu =  True
                if "customKpiWrapperSvc.resources.requests.cpu"  in str(i):
                    wrapper_limit_memory = True
                if "customKpiWrapperSvc.resources.limits.cpu"  in str(i):
                    wrapper_limit_cpu = True

                if "customKpiPyExecSvc.resources.requests.memory"  in str(i):
                    pyexe_request_memory = True
                if "customKpiPyExecSvc.resources.limits.memory"  in str(i):
                    pyexe_request_cpu =  True
                if "customKpiPyExecSvc.resources.requests.cpu"  in str(i):
                    pyexe_limit_memory = True
                if "customKpiPyExecSvc.resources.limits.cpu"  in str(i):
                    pyexe_limit_cpu = True

            if operation == "add":
                customkpi_add_key(customkpi,wrapper_request_memory,wrapper_limit_memory,wrapper_request_cpu,
                                  wrapper_limit_cpu,pyexe_request_memory,pyexe_limit_memory,pyexe_request_cpu,
                                  pyexe_limit_cpu)
            if operation == "delete":
                customkpi_delete_key(customkpi)

            for key,value in data.items():
                if key == "spec":
                    data['spec']['source']['helm']['parameters'] = customkpi
                else:
                    pass


            with open(filepath,mode='w') as f:
                f.write(yaml.safe_dump(data))


        else:
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

    #print("\nupdated chartdir ",chartdir)

    #os.system('cmd /c "helm registry login ghcr.io/bentlynevada-bh/ --username shyam-ks --password ${{ secrets.GH_TOKEN }}')

    for chart,version in chartdir.items():
    #  print("helm pull oci://ghcr.io/bentlynevada-bh/"+chart +" --version "+ version)
    #  print("tar -zxvf ./"+chart+"-"+version+".tgz")
        pass

    print("done")


##################################################################3
def update_value():
    argocddir = os.listdir("argocd")
    helmdir = os.listdir("helm-charts")

    #print("argocddir ",argocddir)
    #print("helmdir ",helmdir)



    for chart  in helmdir:
        for svc in argocddir:
            if chart == "custom-kpi-svc":
                pass
            else:
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

                    try:
                        for key,value in resource.items():
                            if key == "limits":
                                memory_limit = resource['limits']['memory']
                                cpu_limit = resource['limits']['cpu']
                            if key == "requests":
                                memory_request = resource['requests']['memory']
                                cpu_request = resource['requests']['cpu']
                    except:
                        #print("resorce in exception ",resource)
                        #print("chart in exception ",chart)
                        pass

                    filelistnew = []
                    for filename in glob.glob('argocd/'+svc+'/aws/non-prod-2/*.yaml'):
                        filelistnew.append(filename)

                    #print("\nfilelistnew ",filelistnew)

                    for filepath in filelistnew:
                        with open(filepath,mode='r') as f:
                            data = yaml.safe_load(f)


                        if data == None:
                            print("data is none")
                        else:
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



def update__cutomkpi_value():
    argocddir = os.listdir("argocd")
    helmdir = os.listdir("helm-charts")

    #print("argocddir ",argocddir)
    #print("helmdir ",helmdir)
    for chart  in helmdir:
        if chart == "custom-kpi-svc":
            for svc in argocddir:
                if chart == svc:

                    with open("helm-charts/"+chart+"/values.yaml",mode='r') as f:
                        value_data = yaml.safe_load(f)

                    wrapper_resource = {}

                    for key,value in value_data.items():
                        if key == "customKpiWrapperSvc":
                            for wraperkey,wrapervalue in value.items():
                                if wraperkey == "resources":
                                    wrapper_resource.update(wrapervalue)


                    print("\nwrapper_resource ",wrapper_resource)

                    wrapper_memory_limit = ''
                    wrapper_cpu_limit = ''
                    wrapper_memory_request = ''
                    wrapper_cpu_request = ''

                    try:
                        for key,value in wrapper_resource.items():
                            if key == "limits":
                                wrapper_memory_limit = wrapper_resource['limits']['memory']
                                wrapper_cpu_limit = wrapper_resource['limits']['cpu']
                            if key == "requests":
                                wrapper_memory_request = wrapper_resource['requests']['memory']
                                wrapper_cpu_request = wrapper_resource['requests']['cpu']
                    except:
                        #print("resorce in exception ",wrapper_resource)
                        #print("chart in exception ",chart)
                        pass


                    pyexe_resource = {}

                    for key,value in value_data.items():
                        if key == "customKpiPyExecSvc":
                            for pyexekey,pyexevalue in value.items():
                                if pyexekey == "resources":
                                    pyexe_resource.update(pyexevalue)


                    print("\npyexe_resource ",pyexe_resource)

                    pyexe_memory_limit = ''
                    pyexe_cpu_limit = ''
                    pyexe_memory_request = ''
                    pyexe_cpu_request = ''

                    try:
                        for key,value in pyexe_resource.items():
                            if key == "limits":
                                pyexe_memory_limit = pyexe_resource['limits']['memory']
                                pyexe_cpu_limit = pyexe_resource['limits']['cpu']
                            if key == "requests":
                                pyexe_memory_request = pyexe_resource['requests']['memory']
                                pyexe_cpu_request = pyexe_resource['requests']['cpu']
                    except:
                        #print("resorce in exception ",pyexe_resource)
                        #print("chart in exception ",chart)
                        pass



                    filelistnew = []
                    for filename in glob.glob('argocd/'+svc+'/aws/non-prod-2/*.yaml'):
                        filelistnew.append(filename)

                    #print("\nfilelistnew ",filelistnew)

                    for filepath in filelistnew:
                        with open(filepath,mode='r') as f:
                            data = yaml.safe_load(f)


                        if data == None:
                            print("data is none")
                        else:
                            l1 = data['spec']['source']['helm']['parameters']

                            #print("\nbefore l1 ",l1)

                            for i in l1:
                                if "customKpiWrapperSvc.resources.requests.memory"  in str(i):
                                    i['value'] = wrapper_memory_request
                                if "customKpiWrapperSvc.resources.limits.memory"  in str(i):
                                    i['value'] = wrapper_memory_limit
                                if "customKpiWrapperSvc.resources.requests.cpu"  in str(i):
                                    i['value'] = wrapper_cpu_request
                                if "customKpiWrapperSvc.resources.limits.cpu"  in str(i):
                                    i['value'] = wrapper_cpu_limit

                                if "customKpiPyExecSvc.resources.requests.memory"  in str(i):
                                    i['value'] = pyexe_memory_request
                                if "customKpiPyExecSvc.resources.limits.memory"  in str(i):
                                    i['value'] = pyexe_memory_limit
                                if "customKpiPyExecSvc.resources.requests.cpu"  in str(i):
                                    i['value'] = pyexe_cpu_request
                                if "customKpiPyExecSvc.resources.limits.cpu"  in str(i):
                                    i['value'] = pyexe_cpu_limit


                            #print("\nafter l1 ",l1)

                            for key,value in data.items():
                                    if key == "spec":
                                        data['spec']['source']['helm']['parameters'] = l1
                                    else:
                                        pass

                            #print("\nlast data ",data)

                            with open(filepath,mode='w') as f:
                                f.write(yaml.safe_dump(data))


update__cutomkpi_value()
update_value()


#os.system('cmd /c "helm registry login ghcr.io/bentlynevada-bh/ --username shyam-ks --password "'+password)
# os.system('cmd /k "helm pull oci://ghcr.io/bentlynevada-bh/accs-fdn-svc --version 1.0.217"')

#subprocess.run(["helm" , "registry","login", "ghcr.io/bentlynevada-bh/"," --username "," shyam-ks ", " --password  ",password])
