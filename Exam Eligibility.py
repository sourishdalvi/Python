m=str(input("Do you have a medical cause: "))
y=int(input("Enter your age: "))
a=int(input("Enter your attendance: "))
if m=="yesye""Yes" or m=="YES" or m=="yES" or m=="yeS" or m=="YEs" or m=="yEs" or m=="YeS" or m=="YES":
 print("You are eligible for the exam")
else:
 if 13>=y and a>=75:
     print("You are fully eligible for the exam")
 