import name_main

print("top level in second file")

name_main.func()

if __name__ == '__main__':
    print("second file run directly")
else:
    print("second file has been imported")