import yaml
import sys
import re
import base64
import secrets
import string

pattern = r'(keycloak-client-secrets-tenant-)'

print(re.search(pattern, "keycloak-client-secrets-tenant-"))

filename = sys.argv[1]
svc_name = sys.argv[2]
present = False

with open(filename,mode='r') as file:
    data = list(yaml.safe_load_all(file))

for svc in data:
    for key,value in svc.items():
        if key == "data":
            if svc_name in value:
                present = True
                break
            else:
                pass

print("flag ",present)
svc_list = []

if present == False:
    secret_list = []
    l1 = []

    for svc in data:
        for key,value in svc.items():
            if re.search(pattern, svc['metadata']['name']):
                svc_list.append(svc['metadata']['name'])
                break

    print("svc_list ",svc_list)

    for i in svc_list:
        for _ in range(32):
            sec = secrets.choice(string.ascii_letters+string.digits)
            l1.append(sec)
            s1 = ''.join(l1)
        l1 = []
        final_sec = 'sec_' + s1
        secret_list.append(final_sec)

    encoded_list = []
    for i in secret_list:
    #  print(i)
        encoded_string = base64.b64encode(i.encode('utf-8')).decode('utf-8')
        encoded_list.append(encoded_string)

    for i in encoded_list:
        print(i)

    for svc in data:
        for key,value in svc.items():
            if re.search(pattern, svc['metadata']['name']):
                svc['data'][svc_name] = encoded_list.pop()
                print("data ",svc['data'])
                break



    with open(filename,mode='w') as file:
        file.write(yaml.dump_all(data))

