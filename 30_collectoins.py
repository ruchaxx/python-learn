from collections import Counter

l1 = [1,1,1,1,2,2,2,2,3,3,3,3,]
print(Counter(l1))

sentance = "how many times word shows up"
print("sentance ",Counter(sentance.split()))

s1 = "aaassddemkkllxxxxxsjksksss"
c = Counter(s1)
print("c ",c)
print("most_common ",c.most_common())
print("sum of counter value ",sum(c.values()))
print("list of counter ",list(c))

from collections import defaultdict

d = defaultdict(lambda : 0)
d['correct'] = 100
print("value of correct key ",d["correct"])
print("value of wrong key ",d['worng'])

from collections import namedtuple

Dog = namedtuple('Dog',['age','breed','name'])
sammy = Dog(age = 5,breed = 'huskky',name = 'same')
print("sammy ",sammy)
print("sammy age ",sammy.age)