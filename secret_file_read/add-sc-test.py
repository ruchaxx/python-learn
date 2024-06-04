import yaml
import sys
import re
import base64
import secrets
import string

service = sys.argv[1]

svc_name = service.lower().replace("_","-")
print(svc_name+"-secret")

with open("base-file.yaml",mode='r') as f:
    data = list(yaml.safe_load_all(f))

present = True
for svc in data:
    if svc['metadata']['name'] == svc_name+"-secret":
        print("if")
        present = True
    else:
        present = False

l1 = ['1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16']

if present == False:
   data.append({'apiVersion': 'v1', 'data': {'CLIENT_SECRET_A': l1.pop(0), 'CLIENT_SECRET_B': l1.pop(0), 'CLIENT_SECRET_C': l1.pop(0), 'CLIENT_SECRET_D': l1.pop(0), 'CLIENT_SECRET_E': l1.pop(0), 'CLIENT_SECRET_F': l1.pop(0), 'CLIENT_SECRET_G': l1.pop(0), 'CLIENT_SECRET_H': l1.pop(0), 'CLIENT_SECRET_I': l1.pop(0), 'CLIENT_SECRET_J': l1.pop(0), 'CLIENT_SECRET_K': l1.pop(0), 'CLIENT_SECRET_L': l1.pop(0), 
'CLIENT_SECRET_M': l1.pop(0), 'CLIENT_SECRET_N': l1.pop(0), 'CLIENT_SECRET_O': l1.pop(0), 'CLIENT_SECRET_P': l1.pop(0)}, 'kind': 'Secret', 'metadata': {'name': svc_name+"-secret", 'namespace': 'aws-dev'}})

with open("base-file.yaml",mode='w') as f:
    f.write(yaml.dump_all(data))