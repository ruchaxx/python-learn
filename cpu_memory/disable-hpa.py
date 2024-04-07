import yaml
import os,glob
import sys
import subprocess


operation = sys.argv[1]

filelist = []

for filename in glob.glob('argocd/*/aws/non-prod-2/*.yaml'):
    filelist.append(filename)

for filepath in filelist:
    with open(filepath,mode='r') as f:
        data = yaml.safe_load(f)

    #print("\ndata ",data)


    if data == None:
        #print("in iff")
        pass
    else:
        #print("in else....")
        l1 = data['spec']['source']['helm']['parameters']
        for i in l1:
            if "autoscaling.enabled"  in str(i):
                if operation == "enable":
                    if i['value'] == 'false':
                        i['value'] = 'true'
                if operation == "disable":
                    if i['value'] == 'true':
                        i['value'] = 'false'

        for key,value in data.items():
            if key == "spec":
                data['spec']['source']['helm']['parameters'] = l1
            else:
                pass


        with open(filepath,mode='w') as f:
            f.write(yaml.safe_dump(data))

