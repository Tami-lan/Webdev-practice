print("Enter Five subjects marks")
m1=int(input("Enter the mark1: "))
m2=int(input("Enter the mark2: "))
m3=int(input("Enter the mark3: "))
m4=int(input("Enter the mark4: "))
m5=int(input("Enter the mark5: "))

Avg=(m1+m2+m3+m4+m5)/5

if(Avg<=35):
    print("Additional class is required")
else:
    print("You are good to go")