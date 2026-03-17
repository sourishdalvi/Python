try:
    num=int(input("Enter a number: "))
    print("The number you entered is: ", num)
except ValueError as ex:
    print("Exception",ex)       
    