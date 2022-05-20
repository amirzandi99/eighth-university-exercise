def fact_calc(n):
    f = 1
    t = "* "
    if(n > 1):
        t += str(n) + "! = "
        for i in range(1,n+1):
            f *= i
        for i in range(n,0,-1):
            if(i == 1):
                t += str(i)
            else:
                t += str(i) + " x "
    else:
        t += str(n) + "!"
    t += " = " + str(f) + " * "
    return t
# 
while(1):
    try:
        x = int(input("Enter an integer between 0 or 9, -1 to quit => "))
        if(x == -1):
            break
        if(x >= 0 and x <= 9):
            print(fact_calc(x))
        else:
            print("Invalid entry\n")
    except:
        print("Enter an integer number !\n")