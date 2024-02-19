import secrets
import string
import yaml
import base64
import sys

l1 = []
secret_list = []

tenant = sys.argv[1]
num = int(tenant) * 65


for i in range(int(num)):
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
   # print(i)
    pass

with open('base-file.yaml',mode='r') as f:
    data = list(yaml.safe_load_all(f))

#print(data[0])

for i in data:
    for key,value in i.items():
        if key == 'data':
          #  print(value)
            for i,j in value.items():
                try:
                    value[i] = encoded_list.pop()
                except:
                     print("secrets are updated for ",tenant," tenants")

            print("\nupdated \n",value)
            print("\n")


with open("new-base.yaml",mode='w') as f:
    f.write(yaml.safe_dump_all(data))


