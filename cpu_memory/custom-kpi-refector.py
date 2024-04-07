import yaml
import os,glob
import sys

ARGOCD_APPLICATION_PATH = "argocd"
NP_FILE_PATH = "argocd/*/aws/non-prod-2/*.yaml"
operation = sys.argv[1]
password = sys.argv[2]

multi_container_chart = {'custom-kpi-svc':["customKpiWrapperSvc","customKpiPyExecSvc"]}

# if multi_container_chart.get('custom-kpi-svc'):
#     print("in multicontainer if")
#     print(multi_container_chart.get('custom-kpi-svc'))
# else:
#     print("else")

filelist = []

def add_key(l1,chart_name_list,request_memory,limit_memory,request_cpu,limit_cpu):
    container_list = []
    for chart in chart_name_list:
        if multi_container_chart.get(chart):
            #print("in multicontainer if")
            container_list = multi_container_chart.get(chart)
            for container in container_list:
                for i in l1:
                    if container+".resources.requests.memory"  in str(i):
                        request_memory = True
                    if container+"resources.limits.memory"  in str(i):
                        limit_memory =  True
                    if container+"resources.requests.cpu"  in str(i):
                        request_cpu = True
                    if container+"resources.limits.cpu"  in str(i):
                        limit_cpu = True
                if request_memory == False:
                    l1.append({'name': container+'.resources.requests.memory', 'value': ''})
                if limit_memory == False:
                    l1.append({'name': container+'.resources.limits.memory', 'value': ''})
                if request_cpu == False:
                    l1.append({'name': container+'.resources.requests.cpu', 'value': ''})
                if limit_cpu == False:
                    l1.append({'name': container+'.resources.limits.cpu', 'value': ''})
        else:
            if request_memory == False:
                l1.append({'name': 'resources.requests.memory', 'value': ''})
            if limit_memory == False:
                l1.append({'name': 'resources.limits.memory', 'value': ''})
            if request_cpu == False:
                l1.append({'name': 'resources.requests.cpu', 'value': ''})
            if limit_cpu == False:
                l1.append({'name': 'resources.limits.cpu', 'value': ''})

def delete_key(l1,chart_name_list):

    container_list = []
    for chart in chart_name_list:
        if multi_container_chart.get(chart):
            container_list = multi_container_chart.get(chart)
            for container in container_list:
                for i in range(len(l1) -1, -1, -1):
                    if (l1[i]['name'] == container+".resources.requests.memory" or l1[i]['name'] == container+".resources.limits.memory" or  l1[i]['name'] == container+".resources.requests.cpu" 
                        or l1[i]['name'] == container+".resources.limits.cpu"):
                        #print("new ifff")
                        del l1[i]
        else:
            for i in range(len(l1) -1, -1, -1):
                if (l1[i]['name'] == "resources.requests.memory" or l1[i]['name'] == "resources.limits.memory" or  l1[i]['name'] == "resources.requests.cpu" 
                    or l1[i]['name'] == "resources.limits.cpu"):
                    #print("new ifff")
                    del l1[i]


def update_value(chart_name_list):
    #print("\nin update function")
    argocddir = os.listdir(ARGOCD_APPLICATION_PATH)
    helmdir = os.listdir("helm-charts")

    #print("chart_name_list ",chart_name_list)

    #print("argocddir ",argocddir)
    #print("helmdir ",helmdir)



    for chart  in helmdir:
        for svc in argocddir:
                if chart == svc:

                    with open("helm-charts/"+chart+"/values.yaml",mode='r') as f:
                        value_data = yaml.safe_load(f)

                    resource = {}
                    container_resource = {}
                    container_list = []

                    for chart_list in chart_name_list:
                        if multi_container_chart.get(chart_list):
                            print("in multicontainer if ",chart_list)
                            container_list = multi_container_chart.get(chart_list)
                            for container in container_list:
                                for key,value in value_data.items():
                                    if key == container:
                                        for resourcekey,resourcevalue in value.items():
                                            if resourcekey == "resources":
                                                container_resource.update(resourcevalue)


                                container_memory_limit = ''
                                container_cpu_limit = ''
                                container_memory_request = ''
                                container_cpu_request = ''

                                if container_resource == None:
                                    pass
                                else:
                                    try:
                                        for key,value in container_resource.items():
                                            if key == "limits":
                                                container_memory_limit = container_resource['limits']['memory']
                                                container_cpu_limit = container_resource['limits']['cpu']
                                            if key == "requests":
                                                container_memory_request = container_resource['requests']['memory']
                                                container_cpu_request = container_resource['requests']['cpu']
                                    except:
                                        #print("resorce in exception ",resource)
                                        #print("chart in exception ",chart)
                                        pass

                                    filelistnew = []
                                    for filename in glob.glob('argocd/'+chart_list+'/aws/non-prod-2/*.yaml'):
                                        filelistnew.append(filename)

                                    #print("\nmultivontainer ",filelistnew)

                                    for filepath in filelistnew:
                                        with open(filepath,mode='r') as f:
                                            data = yaml.safe_load(f)

                                        if data == None:
                                            print("data is none in update func for ",filepath)
                                        else:
                                            l1 = data['spec']['source']['helm']['parameters']

                                            #print("\nbefore l1 ",l1)

                                            if container_resource.get('requests') and container_resource.get('limits'):

                                                for i in l1:
                                                    if container+".resources.requests.memory"  in str(i):
                                                        i['value'] = container_memory_request
                                                        print("in if memory_request ",container_memory_request)
                                                    if container+".resources.limits.memory"  in str(i):
                                                        i['value'] = container_memory_limit
                                                    if container+".resources.requests.cpu"  in str(i):
                                                        i['value'] = container_cpu_request
                                                    if container+".resources.limits.cpu"  in str(i):
                                                        i['value'] = container_cpu_limit


                                                #print("\nafter l1 ",l1)
                                                for key,value in data.items():
                                                        if key == "spec":
                                                            data['spec']['source']['helm']['parameters'] = l1
                                                        else:
                                                            pass

                                                    #print("\nlast data ",data)
                                                with open(filepath,mode='w') as f:
                                                        #print("in write func")
                                                    f.write(yaml.safe_dump(data))
                                                        #print("\nvalue is updated in file........." , data)
                                                    #print(chart+" is updated")

                        else:
                            #print("in else ",chart_list)
                            for key,value in value_data.items():
                                if key == "resources":
                                    resource.update(value)


                            #print("\nresource in update func",resource)

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

                            filelist_new = []
                            if multi_container_chart.get(svc):
                                #print("in skip if")
                                pass
                            else:

                                for filename in glob.glob('argocd/'+svc+'/aws/non-prod-2/*.yaml'):
                                    filelist_new.append(filename)

                                    #print("\nfilelistnew ",filelist_new)
                                for filepath in filelist_new:
                                    with open(filepath,mode='r') as f:
                                        data = yaml.safe_load(f)

                                    if data == None:
                                        print("data is none in update func for ",filepath)
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
                                                #print("in write func")
                                            f.write(yaml.safe_dump(data))
                                                #print("\n else  value is updated in file.........",data)
                                            #print(chart+" is updated")



print("\nupdate function call.........")


def download_chart():
    dirlist = []
    dirlist = os.listdir(ARGOCD_APPLICATION_PATH)

    #print("dirlist ",dirlist)

    chartdir = {}

    for i in dirlist:
        chartdir[i] = ''

    #print("chartdir ",chartdir)

    for filename in glob.glob(NP_FILE_PATH):
        filelist.append(filename)


    for filepath in filelist:
        with open(filepath,mode='r') as f:
            data = yaml.safe_load(f)

        if data == None:
            print("data is none for ",filepath)
            with open("output.txt",mode='a') as f:
                    f.write("menifest file is comment out for  "+filepath+"\n")
        else:
            for chart,version in chartdir.items():
                    for key,value in data.items():
                        try:
                            if data['spec']['source']['chart'] == chart:
                                chartdir[chart] = data['spec']['source']['targetRevision']
                            else:
                                pass
                        except:
                            pass  #common-metadata,rc-23-4


    os.system("helm registry login ghcr.io/bentlynevada-bh/ --username shyam-ks --password "+password)
    os.system("pwd")
    os.system("mkdir helm-charts")

    for chart,version in chartdir.items():
        os.system("helm pull oci://ghcr.io/bentlynevada-bh/"+chart +" --version "+ version)
        os.system("tar -zxvf ./"+chart+"-"+version+".tgz")
        os.system("cp -r ./"+chart+" helm-charts")

########################################################################

print("starting...............................")



for filename in glob.glob(NP_FILE_PATH):
    filelist.append(filename)


for filepath in filelist:
    with open(filepath,mode='r') as f:
        data = yaml.safe_load(f)

    if data == None:
        pass
    else:
        try:
                    l1 = data['spec']['source']['helm']['parameters']
                    chart_name_list = []
                    chart_name_list.append(data['spec']['source']['chart'])


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


                    #print("operation ",operation)
                    if operation == "add":
                        #download_chart()
                        add_key(l1,chart_name_list,request_memory,limit_memory,request_cpu,limit_cpu)
                        for key,value in data.items():
                            if key == "spec":
                                data['spec']['source']['helm']['parameters'] = l1
                            else:
                                pass

                        #print("filepath ",filepath)
                        with open(filepath,mode='w') as f:
                            f.write(yaml.safe_dump(data))

                        update_value(chart_name_list)
                    if operation == "delete":
                        #print("in delete if")
                        delete_key(l1,chart_name_list)
                        print("delete list ",l1)


                        for key,value in data.items():
                            if key == "spec":
                                data['spec']['source']['helm']['parameters'] = l1
                            else:
                                pass

                        print("filepath ",filepath)
                        with open(filepath,mode='w') as f:
                            f.write(yaml.safe_dump(data))
        except:
            pass


    #print("\nupdated chartdir ",chartdir)


