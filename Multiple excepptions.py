try:
 num1,num2=eval(input("Enter the numbers separated by a coma: "))
 result=num1/num2
 print("the result is: ",result)
except ZeroDivisionError:
    print("You can't divide by zero")
except SyntaxError:
    print("comma is missing please enter the numbers to be separated by a coma")
except:
    print("Invalid input, please enter valid numbers")
finally:
    print("This block will always be executed")