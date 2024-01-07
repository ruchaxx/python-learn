import yaml
import base64

def decode_value(encoded_dict):
    decoded_dict = {}
    for (i,j) in encoded_dict.items():
        print("j in dict ",j)
        decoded_bytes = base64.b64decode(j)
        decoded_string = decoded_bytes.decode('utf-8')
        decoded_dict[i] = decoded_string
    return decoded_dict

with open('multiple_secret.yaml',mode='r') as original_file:
    data1 = list(yaml.safe_load_all(original_file))

print("\ndata1 ",data1)
# data = {}
# for i in data1:
#     print("\ni in for loop ",i)
#     data.update(i)
#     print("\ndata  in for loop ",data)

# print("\ndata ",data)
final_decoded_dict = {}
final_list = []

for data in data1:
    for (key,value) in data.items():
        print("\nkey in for ",key)
        if key == 'data':
           # print("\nkey is ",key)
           # print("\nvalue is ",value)
            final_decoded_dict = decode_value(value)
          #  print("\ndecoded_dict ",final_decoded_dict)
            data[key] = final_decoded_dict
          #  print("\nfinal data ",data)
            final_list.append(data)
        else:
            pass

print("\nfinal list ",final_list)

with open('decode-multiple-secret.yaml',mode='w') as decode_file:
    decode_file.write(yaml.safe_dump_all(final_list))

