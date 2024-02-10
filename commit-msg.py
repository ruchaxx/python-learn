import sys
import re

msg = sys.argv[1]
print("commit msg ",msg)

# commit_conv = msg.split('(')
# print("commit_conv ",commit_conv)

# space = msg.split('):')
# print("space ",space)

# l2 = ['docs','feat','fix','perf','refactor','style','test','build','ci','chore','revert']

# if commit_conv[0] in l2:
#     print("message convension is correct")
# else:
#     raise Exception("message convension is not correct")


pattern = r'["\']'

quotes = re.search(pattern, msg)
print("matches  ",type(quotes))

fix = re.search(r"\bfix\b\(\d+\): [a-z,A-Z,0-9,\s]*", msg)
docs = re.search(r"\bdocs\b\(\d+\): [a-z,A-Z,0-9,\s]*", msg)
feat = re.search(r"\bfeat\b\(\d+\): [a-z,A-Z,0-9,\s]*", msg)
chore = re.search(r"\bchore\b\(\d+\): [a-z,A-Z,0-9,\s]*", msg)
perf = re.search(r"\bperf\b\(\d+\): [a-z,A-Z,0-9,\s]*", msg)
refactor = re.search(r"\brefactor\b\(\d+\): [a-z,A-Z,0-9,\s]*", msg)
style = re.search(r"\bstyle\b\(\d+\): [a-z,A-Z,0-9,\s]*", msg)
test = re.search(r"\btest\b\(\d+\): [a-z,A-Z,0-9,\s]*", msg)
build = re.search(r"\bbuild\b\(\d+\): [a-z,A-Z,0-9,\s]*", msg)
ci = re.search(r"\bci\b\(\d+\): [a-z,A-Z,0-9,\s]*", msg)
revert = re.search(r"\brevert\b\(\d+\): [a-z,A-Z,0-9,\s]*", msg)

print("fix ",fix)


if (fix or docs or feat or chore or perf or refactor or style or test or build or ci or revert) and (quotes is None):
    print("message convension is correct")
else:
    raise Exception("message convension is not correct")