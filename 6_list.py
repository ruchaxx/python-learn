lists = ['string',100,23.2]
print(len(lists))
print(lists)

help(lists.insert)

#indexing
print(lists[1])

#slicing
print("slicing on list ",lists[1:])


#concatinating
list1 = ['one', 'two', 'three']
list2 = ['four', 'five']
list3 = list1 + list2
print(list3)

#mutable
list3[0] = "ONE ALL CAPS"
print(list3)

#add items at the end
list3.append('six')
list3.append('seven')
print(list3)

#remove items at the end
list3.pop()
poped_item = list3.pop()
print(poped_item)
print(list3)

list3.pop(2)

#sorting
num_list = [4,2,6,1]
num_list.sort()
print("sorting ",num_list)

#reversing
num_list = [4,2,6,1]
num_list.reverse()
print("reversing ",num_list)

#indexing nested list
nested_list =  [1,1,[1,2]]
print("indexing nested list ",nested_list[2][1])