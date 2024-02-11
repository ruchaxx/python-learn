import math
import random

#help(math)

value = 4.35
print("floor ",math.floor(value))
print("ceil ",math.ceil(value))
print("round ",round(value))
print("sin ",math.sin(10))


print("random number ",random.randint(0,100))

random.seed(101)
print("seed_example ",random.randint(0,101))

l1 = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]
print("choice ",random.choice(l1))
print("sample with replacement ",random.choices(population=l1,k=8))
print("sample without replacement ",random.sample(population=l1,k=8))

random.shuffle(l1)
print("shuffle list ",l1)

print("uniform ",random.uniform(a=0,b=100))

print("gauss ",random.gauss(mu=0,sigma=1))