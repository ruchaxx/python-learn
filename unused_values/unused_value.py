import yaml
import os, glob
 
with open("accs-fdn-svc/values.yaml",'r') as f:
    data = yaml.safe_load(f)
 
 
unused_value = []
unused_value_dict = []
final_unused_value = []
 
 
dataitems = list(data.items())
print("\nlist of items ",dataitems)
nested_key = []
new_list = []
nested_dic = {}
keyj = []
 
 
found = False
found_in_dict = False
found_in_dict_one = False
 
for (i,j) in dataitems:
     print("\nj type ",type(j))
     print("\nj  ",j)
     if (type(j)) == dict:
          print("dict")
          for filename in glob.glob('accs-fdn-svc/*/*.*'): #config ,deployment
              with open(os.path.join(os.getcwd(), filename), 'r') as files:
                lines = files.read()
              if lines.find('.Values.{}.'.format(i)) != -1:
                  new_list = []
                  print("\nwhole dict is not used  ",'.Values.{}.'.format(i))
                  nested_key.append(list(j.keys()))
                  print("\nnested keys",nested_key)
                  for y in nested_key:
                    new_list.extend(y)
                  nested_key = []
                  print("\nnew list ",new_list)
                  for x in new_list:
                    print("\nin dict before if for keys  ",'.Values.{}.{}'.format(i,x))
                    if lines.find('.Values.{}.{}'.format(i,x)) != -1:  #.Values.image.name
                        print("\nin dict if for keys  ",'.Values.{}.{}'.format(i,x))
                        found_in_dict = True
                    else:
                        #found_in_dict = False
                        continue
                    print("\nfound_in_dict ",found_in_dict)
                    print("\nunused_value_dict after if ",unused_value_dict)
              elif lines.find('.Values.{}'.format(i)) != -1:
                   print("\ndict used ",'.Values.{}'.format(i))
                   found_in_dict = True
                   break
              else:
                   #print("\ndict used ",'.Values.{}'.format(i))
                   #found_in_dict = False
                   continue
          print("\nfound_in_dict befor append ",found_in_dict)
          if not found_in_dict:
              unused_value_dict.append(i)
          print("\nunused_value_dict after if not....... ",unused_value_dict)
     else:
          for filename in glob.glob('accs-fdn-svc/*/*.*'): #config ,deployment
              with open(os.path.join(os.getcwd(), filename), 'r') as files:
                lines = files.read()
              if lines.find('.Values.{}'.format(i)) != -1:
                   print("\nin if condition ",'.Values.{}'.format(i))
                   found = True
                   break
              else:
                   found = False
                   continue
          if not found:
              unused_value.append(i)
 
final_unused_value = unused_value + unused_value_dict
print("\nfinal_unused_value ",final_unused_value)
 
if final_unused_value == []:
       print("\nall values are used")
else:
    print("\nunused value ",final_unused_value)