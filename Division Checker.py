a=int(input("Enter a number to be divided"))
b=int(input("Enter a number to divide by"))
if b!=0 and a%b==0:
 print("Division between both numbers given is possible,result of",a,"divided by",b,"is:",a//b)
elif b==0:
  print("Division by zero is not possible")
else :
  print(a,"is not divisible by",b)
  


   
