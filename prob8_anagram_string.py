str1 = input("Enter first string ")
str2 = input("Enter second string ")


str1_list = list(str1)
str2_list = list(str2)
str3_list = []

for i in str1_list:
    for j in str2_list:
        if i == j:
            str3_list.append(i)
            break
        else:
            continue

if str1_list == str3_list:
    print("anagram")
else:
    print("not anagram")