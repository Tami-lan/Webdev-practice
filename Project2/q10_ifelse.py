a=int(input("Enter the 1st number:"))
b=int(input("Enter the 2nd number:"))
ops=input("Enter the operation to do 1.add 2.sub 3.mul 4.div:")
if (ops=="add"):
    print(a+b)
elif (ops=="sub"):
    print(a-b)
elif(ops=="mul"):
    print(a*b)
elif(ops=="div"):
    print(a/b)
else:
    print("Invalid operation")
