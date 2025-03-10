score=int(input("Enter the score percentage to find eligibility:"))
if(score>=70):
    print("You are Eligible")
    name=input("Enter the name:")
    department=input("Enter the department:")
    location=input("Enter the location:")
else:
    print("You are not Eligible")