import yaml
import base64
import sys

file_name = sys.argv[1]
flag = sys.argv[2]

def decode_value(encoded_dict):
    decoded_dict = {}
    for (i,j) in encoded_dict.items():
        print("j in dict ",j)
        decoded_bytes = base64.b64decode(j)
        decoded_string = decoded_bytes.decode('utf-8')
        decoded_dict[i] = decoded_string
    return decoded_dict

def encoded_value(decoded_dict):
    encoded_dict = {}
    for (i,j) in decoded_dict.items():
        print("j in dict ",j)
        encoded_string = base64.b64encode(j.encode('utf-8')).decode('utf-8')
        encoded_dict[i] = encoded_string
    return encoded_dict

with open(file_name,mode='r') as original_file:
    data1 = list(yaml.safe_load_all(original_file))

print("\ndata1 ",data1)

# data = {}
# for i in data1:
#     print("\ni in for loop ",i)
#     data.update(i)
#     print("\ndata  in for loop ",data)

# print("\ndata ",data)
final_dict = {}
final_list = []

for data in data1:
    for (key,value) in data.items():
        print("\nkey in for ",key)
        if key == 'data':
           # print("\nkey is ",key)
           # print("\nvalue is ",value)
            if flag == '-e':
                final_dict = encoded_value(value)
            elif flag == '-d':
                final_dict = decode_value(value)
            else:
                print("enter correct flag")
                exit()
          #  print("\ndecoded_dict ",final_dict)
            data[key] = final_dict
          #  print("\nfinal data ",data)
            final_list.append(data)
        else:
            pass

print("\nfinal list ",final_list)

with open('sample-secret.yaml',mode='w') as decode_file:
    decode_file.write(yaml.safe_dump_all(final_list))

