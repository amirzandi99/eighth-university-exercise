x = str(input("input string 1 : "))
y = str(input("input string 2 : "))
first = []
last = []
c = 0
if(x == y):
    print("two string is equal")
else:
    for i in range(len(x)):
        if(x[i] == y[0]):
            k = i
            r = i
            t = 1
            for j in range(len(y)):
                if(k == len(x)):
                    break
                if(x[k] == y[j]):
                    k += 1
                else:
                    t = 0
                    break
            if(t == 1):
                first.append(r)
                last.append(k)
                c += 1
    print(f"count : {c}")
    for i in range(c):
        print(f"index : {first[i]} to {last[i]}")