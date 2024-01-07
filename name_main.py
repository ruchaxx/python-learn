def func():
    print("func in name_main")

print("top level in name_main file")

if __name__ == '__main__':
    print("name_main.py run directly")
else:
    print("name_main.py has been imported")