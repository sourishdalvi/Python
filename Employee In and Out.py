class Employee:
    def __init__(self):
        print("Employee created")
    def __del__(self):
        print("Destructor created")
def Create_obj():
    print("Creating object")
    obj=Employee()
    print("Function end")
    return obj
print("Calling function")
obj=Create_obj()
print("Program end")