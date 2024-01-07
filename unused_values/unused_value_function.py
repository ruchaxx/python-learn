import yaml
import os, glob
import sys

chart_name = sys.argv[1]
values_file = sys.argv[2]
with open(chart_name+'/'+values_file,'r') as f:
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


def iterate_dict(item_key,item_value,nested_key,new_list):
    for filename in glob.glob(chart_name+'/*/*.*'): #config ,deployment
              with open(os.path.join(os.getcwd(), filename), 'r') as files:
                lines = files.read()
              nested_key = []
              new_list = []
              if lines.find('.Values.{}.'.format(item_key)) != -1:
                  new_list = []
                  print("\nwhole dict is not used  ",'.Values.{}.'.format(item_key))
                  nested_key.append(list(item_value.keys()))
                  print("\nnested keys",nested_key)
                  for nested_key_element in nested_key:
                    new_list.extend(nested_key_element)
                  nested_key = []
                  print("\nnew list ",new_list)
                  for new_list_element in new_list:
                    print("\nin dict before if for keys  ",'.Values.{}.{}'.format(item_key,new_list_element))
                    if lines.find('.Values.{}.{}'.format(item_key,new_list_element)) != -1:  #.Values.image.name
                        print("\nin dict if for keys  ",'.Values.{}.{}'.format(item_key,new_list_element))
                        found_in_dict = True
                    else:
                        found_in_dict = False
                        continue
                    print("\nfound_in_dict ",found_in_dict)
                    print("\nunused_value_dict after if ",unused_value_dict)
              elif lines.find('.Values.{}'.format(item_key)) != -1:
                   print("\ndict used ",'.Values.{}'.format(item_key))
                   found_in_dict = True
                   break
              else:
                   #print("\ndict used ",'.Values.{}'.format(i))
                   #found_in_dict = False
                   continue

    print("\nfound_in_dict in def ",found_in_dict)
    return found_in_dict

def iterate_list(item_key,item_value,nested_key,new_list):
    for filename in glob.glob(chart_name+'/*/*.*'): #config ,deployment
              with open(os.path.join(os.getcwd(), filename), 'r') as files:
                lines = files.read()
              print("\n############## ",'with .Values.{}'.format(item_key))
              if lines.find('with .Values.{}'.format(item_key)) != -1: #with .Values.imagePullSecrets
                  print("\nwhole list is used")
              else:
                  for element in item_value:
                      if (type(element)) == dict:
                           found_in_dict = iterate_dict(item_key,item_value,nested_key,new_list)

    print("\nfound_in_dict in def ",found_in_dict)
    return found_in_dict


for (item_key,item_value) in dataitems:
     print("\nitem_value type ",type(item_value))
     print("\nitem_value  ",item_value)
     if (type(item_value)) == dict:
          print("dict")
          found_in_dict = iterate_dict(item_key,item_value,nested_key,new_list)
          print("\nfound_in_dict befor append ",found_in_dict)
          if not found_in_dict:
              unused_value_dict.append(item_key)
          print("\nunused_value_dict after if not....... ",unused_value_dict)
     elif (type(item_value)) == list:
         print("list")
         found_in_dict = iterate_list(item_key,item_value,nested_key,new_list)
         print("\nfound_in_dict befor append ",found_in_dict)
         if not found_in_dict:
            unused_value_dict.append(item_key)
            print("\nunused_value_dict after if not....... ",unused_value_dict)
     else:
          for filename in glob.glob('accs-fdn-svc/*/*.*'): #config ,deployment
              with open(os.path.join(os.getcwd(), filename), 'r') as files:
                lines = files.read()
              if lines.find('.Values.{}'.format(item_key)) != -1:
                   print("\nin if condition ",'.Values.{}'.format(item_key))
                   found = True
                   break
              else:
                   found = False
                   continue
          if not found:
              unused_value.append(item_key)

final_unused_value = unused_value + unused_value_dict
print("\nfinal_unused_value ",final_unused_value)

if final_unused_value == []:
       print("\nall values are used")
else:
    print("\nunused value ",final_unused_value)