#Converts entered binary number to decimal
#Detects any invalid input
#has floating point support


digit=str(input("Enter binary to be converted into Decimal,Enter -1 to exit:\n"))
while(digit!="-1"):#dummy is -1
    sumf=0
    indcount=0
    countd=countf=1
    errcount=0
    for ind in digit:
        if(ind=="."):
            indcount=1
        elif(ind not in("1","0")):#cannot use "or" or "and"
            errcount=1 #If wrong input, output isnt printed
    if(indcount==0):
        for x in digit:
            val=int(x)*(2**(len(digit)-countf))
            sumf=sumf+val
            countf+=1
    else:
        digit=digit.split(".")
        front=digit[0]
        deli=digit[1]
        for y in deli:
            val=int(y)*(1/(2**countd))
            sumf=sumf+val
            countd+=1
        for x in front:
            val=int(x)*(2**(len(front)-countf))
            sumf=sumf+val
            countf+=1
    if(errcount==0):
        print(sumf)
    else:
        print("Wrong Input")
    digit=str(input("Enter binary to be converted into Decimal:\n"))