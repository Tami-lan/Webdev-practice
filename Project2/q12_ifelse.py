Salary=int(input("Enter your salary:"))
age=int(input("Enter your age"))
if((Salary>=20000)or (age<=25)):
    ln_am=int(input("Enter the loan amount:"))
    if(ln_am<=50000):
        print("Your are eligible for loan")
    else:
        print("Maximum loan amount is 50000")
else:
    print("You are not eligible for loan")