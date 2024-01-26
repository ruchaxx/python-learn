#Advance Number

print(hex(12))
print(bin(1223))
print(pow(2,4))
print(abs(-3))
print(round(3.1))
print(round(3.14562728,2))


#Advance String

s = 'hello world'
print(s.capitalize())
print(s.upper())
print(s.lower())
print(s.count('o'))
print(s.find('o'))
print(s.center(20,'z'))

s1 = 'hello'
print(s1.isalnum())
print(s1.isalpha())
print(s1.islower())
print(s1.isspace())
print(s1.istitle())
print(s1.isupper())
print(s1.endswith('o'))
print(s1.split('e'))   #every instance
print(s1.partition('e'))  #first instance

#Advance Sets
s = set()
s.add(1)
s.add(2)
print(s)
s.clear()

s = {1,2,3,4}
sc = s.copy()
s.add(5)
print("differance ",s.difference(sc))

s1 = {1,2,3}
s2 = {1,4,5}
s1.difference_update(s2)
print(s1)

s.discard(5)

s1 = {1,2,3}
s2 = {1,4,5}
print("\nintersection ",s1.intersection(s2))
s1.intersection_update(s2)
print("s1 after intersection_update ",s1)

s1 = {1,2,3}
s2 = {1,2,4}
s3 = {5}
print("disjoint ",s1.isdisjoint(s2))
print("is subset ",s1.issubset(s2))
print("symetric_diffrence ",s1.symmetric_difference(s2))
print("union ",s1.union(s2))
s1.update(s2)
print("s1 after update ",s1)

#Advance Dict

d = {'k1':1,'k2':2}
print("\ndict comprehension ",{x:x**2 for x in range(10)})

#Advance List

l = [1,2,3]
x = [1,2,3]
x.append([4,5])
print("\nafter append",x)

x = [1,2,3]
x.extend([4,5])
print("after extenad",x)

print("index",l.index(1))
l.insert(2,'inserted') # 2 arg require
print("l after insert ",l)
l.remove('inserted')  #remove 1st instance only
print("l after remove ",l)
l.reverse()
print("l after reverse ",l)
l.sort()
print("sorting ",l)

