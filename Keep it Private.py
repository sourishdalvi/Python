class Myclass:
    __private_var = 27
    def __PrivateMethod(self):
        print("Im inside my class")
    def hello (self):
        print ("private var is ", Myclass.__private_var)
foo= Myclass()
foo.hello()
foo.__PrivateMethod()

