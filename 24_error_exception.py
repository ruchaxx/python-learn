try:
    with open('testfile.txt',mode='w') as f:
        f.write("this is test file")
except TypeError:
    print("there is type error")
except OSError:
    print("os error")
except:
    print("all other exceprion")
finally:
    print("I alwasy run")


#try block in fuction

def ask_int():
    while True:
        try:
            result = int(input("enter number "))
        except:
            print("not num")
            continue
        else:
            print("else block")
            break
        finally:
            print("finally block of ask_int()")

ask_int()