import yaml

# with open('sample.yaml',mode='r') as f:
#     data = yaml.safe_load_all(f)

# print(data)

def read_file():
    yamlfile = open('sample.yaml','r')
    data = yaml.safe_load(yamlfile)
    return data

filedata = read_file()
print("filedata ",filedata)
print("\nkeys ",filedata.keys())
print("\nvalues ",filedata.values())
print("\nitems ",filedata.items())