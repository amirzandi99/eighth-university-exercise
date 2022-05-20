word = ["smile", "discuss", "confess", "declare", "laugh", "run", "cough", "teach", "buy"]
temp = []
test = []
l = len(word)
for i in range(l):
    temp.append(word[i])
for i in range(l):
    x = len(word[i])
    w = word[i]
    if(w[x-1] == 'e'):
        temp[i] = word[i] + 'd'
        test.append(1)
    elif(w[x-2] == 's' and w[x-1] == 's'):
        temp[i] = word[i] + 'ed'
        test.append(1)
    elif(w[x-2] == 'g' and w[x-1] == 'h'):
        temp[i] = word[i] + 'ed'
        test.append(1)
    else:
        test.append(0)
for i in range(l):
    if(test[i] == 1):
        print(f"{word[i]}\t: {temp[i]}")
    else:
        print(f"{word[i]}\t: Irregular past tense verb")