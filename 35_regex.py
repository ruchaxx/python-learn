import re

text = "the agent phone no is 408-555-1234.call soon"

pattern = 'phone'
print(re.search(pattern,text))

text2 = 'my phone once , my phone two'
pattern2 = 'phone'
matches = re.findall(pattern,text2)
print("matches ",matches)

for match in re.finditer('phone',text2):
    print(match.group())

phone = re.search('\d+-\d+-\d+',text)
print("phone ",phone)

phone_pattern = re.compile(r'(\d{3})-(\d{3})-(\d{4})')
result = re.search(phone_pattern,text)
print("group ",result.group())
print("first group ",result.group(1))

print("or opertator ",re.search(r'cat|dog','cat is here'))
print("wildcartd opertator ",re.findall(r'.at','cat is sat at here'))
print("text start with num  ",re.findall(r'^\d','7 cat is sat at here'))
print("text end with num  ",re.findall(r'\d$','cat is sat at here 9'))


phase = "there are 3 nums 34 inside 5 this sentence"
pattern = r'[^\d]+'  # exclude digit (exclude karava [] ma lakhavu)
print("exculde num  ",re.findall(pattern,phase))

clean = re.findall(pattern,phase)
print("join = ",' '.join(clean))


text = "only find hypen-word in sentence.but you do-not know how"
pattern = r'[\w]+-[\w]+'
print(re.findall(pattern,text))

t1 = 'catfish'
print(re.search(r'cat(nap|fish|claw)',t1))


