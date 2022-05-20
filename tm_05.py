fileName = "tm_05t.txt"
firstname = []
middlename = []
surname = []
myFile = open(fileName,"r")
note = myFile.readlines()
for i in note:
    tmp = ""
    flag = 1
    t = 0
    for j in range(len(i)):
        if(flag == 1):
            if(i[j] == ','):
                surname.append(tmp)
                tmp = ""
                flag += 1
            else:
                tmp += i[j]
        if(flag == 2):
            if(i[j] == ' '):
                t += 1
            else:
                if(t == 2 or i[j] == '.'):
                    middlename.append(tmp)
                    tmp = ""
                    flag += 1
                elif(t == 1):
                    tmp += i[j]
        if(flag == 3):
            if(i[j] == ' '):
                t += 1
            elif(i[j] == '.' and tmp != ''):
                firstname.append(tmp)
                tmp = ""
            elif(t == 2):
                tmp += i[j]
for i in range(len(note)):
    print ("{:<24} {:<10} {:<10}".format(surname[i], middlename[i], firstname[i]))