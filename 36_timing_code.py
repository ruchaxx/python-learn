def func1(n):
    return [str(num) for num in range(n)]

print("func1 ",func1(10))

def func2(n):
    return list(map(str,range(n)))

print("func2 ",func2(10))

import time

#Current time before
stat_time = time.time()

#Run code
result = func1(1000000)

#Current time after running code
end_time = time.time()

#Elapsed time
elapsed_time = end_time - stat_time

print("elapsed time for func1",elapsed_time)

#Current time before
stat_time = time.time()

#Run code
result = func2(1000000)

#Current time after running code
end_time = time.time()

#Elapsed time
elapsed_time = end_time - stat_time

print("elapsed time for func2",elapsed_time)

#####################################################################################

import timeit

stmt = '''
func1(100)
'''

setup = '''
def func1(n):
    return [str(num) for num in range(n)]
'''

print("timeit for func1 ",timeit.timeit(stmt,setup,number=100000))

stmt2 = '''
func2(100)
'''

setup2 = '''
def func2(n):
    return [str(num) for num in range(n)]
'''

print("timeit for func2 ",timeit.timeit(stmt2,setup2,number=100000))

