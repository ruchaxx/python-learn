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

with open('secret.yaml',mode='r') as original_file:
    data = yaml.safe_load(original_file)

print("data ",data)
final_decoded_dict = {}

for (key,value) in data.items():
    print("\nkey in for ",key)
    if key == 'data':
        print("\nkey is ",key)
        print("\nvalue is ",value)
        final_decoded_dict = decode_value(value)
        print("\ndecoded_dict ",final_decoded_dict)
        data[key] = final_decoded_dict
    else:
        pass

print("final data ",data)

with open('decode-secret.yaml',mode='w') as decode_file:
    decode_file.write(yaml.safe_dump(data))

