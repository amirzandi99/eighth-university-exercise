name = []
family = []
age = []
x = int(input("input number of person : "))
for i in range(x):
    n = str(input("input name   : "))
    f = str(input("input family : "))
    a = int(input("input age    : "))
    print("")
    name.append(n)
    family.append(f)
    age.append(a)
print("\nOriginal list")
for i in range(20):
    print("-", end='')
print("")
for i in range(x):
    print(f"\t{family[i]}, {name[i]}\t{age[i]}")
# 
for i in range(x):
    for j in range(x):
        if(j < x-1):
            n1 = family[j]
            n2 = family[j+1]
            if(ord(n1[0]) > ord(n2[0])):
                temp = name[j]
                name[j] = name[j+1]
                name[j+1] = temp
                # 
                temp = family[j]
                family[j] = family[j+1]
                family[j+1] = temp
                # 
                temp = age[j]
                age[j] = age[j+1]
                age[j+1] = temp
            elif(ord(n1[0]) == ord(n2[0])):
                if(ord(n1[1]) > ord(n2[1])):
                    temp = name[j]
                    name[j] = name[j+1]
                    name[j+1] = temp
                    # 
                    temp = family[j]
                    family[j] = family[j+1]
                    family[j+1] = temp
                    # 
                    temp = age[j]
                    age[j] = age[j+1]
                    age[j+1] = temp
# 
print("\nAlphabetized list")
for i in range(20):
    print("-", end='')
print("")
for i in range(x):
    print(f"\t{family[i]}, {name[i]}\t{age[i]}")