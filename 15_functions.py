def say_hello():
    print("hello")

say_hello()

#function override
def say_hello(name='default'):
    print(f"hello {name}")

say_hello("rucha")

#return --->  result var ma save kare (print save nai kare)
def sum(n1,n2):
    return n1 + n2

result = sum(1,3)
print("sum ",result)

def even(num):
    return  num % 2 == 0

even(30)

#return even num list
def check_even_list(num_list):
    even_list = []
    for i in num_list:
        if i % 2 == 0:
             even_list.append(i)
        else:
            pass
    return even_list  # return for ni bahar lakhay

l1 = [2,3,4,5,6,7]
result = check_even_list(l1)
print(result)

#tuple unpacking
work_hour = [('a',200),('b',100),('c',400)]

def emp_check(work_hour):
    current_max = 0
    emp_of_month = ''
    for emp,hour in work_hour:
        if hour > current_max:
            current_max = hour
            emp_of_month = emp
        else:
            pass

    return (emp_of_month,current_max)

result = emp_check(work_hour)
name,hours = emp_check(work_hour)
print(result)
print(name)
print(hours)