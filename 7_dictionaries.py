my_dict = {'name':'Rucha'}
print(my_dict)
print(my_dict['name'])

#nested dict
d = {'k1': 123,'k2': [0,1,2],'k3':{'inside':'100'}}
print(d['k3']['inside'])
print(d['k2'][2])

#insert new key
d = {'k1': 100,'k2': 200}
d['k3'] = 300
print(d)

#override existing value of key
d['k1'] = 'new value'
print(d)

#functions
print("keys ",d.keys())      #tupple
print("values ",d.values())  #tupple
print("items ",d.items())    #tupple