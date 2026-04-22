class IOString():
 def __init__(self,):
    self.s = ""
 def get_string(self):
        self.s = input("Enter a string: ")
 def input_string(self):
            self.s = input("Enter a string: ")
 def print_string(self):
                print(self.s.upper())
s = IOString()
s.get_string()
s.print_string()