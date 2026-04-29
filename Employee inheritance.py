class Person(object):
    def __init__(self, name, id_number):
        self.name = name
        self.id_number = id_number

    def display(self):
        print("Name:", self.name)
        print("ID Number:", self.id_number)
class Employee(Person):
        def __init__(self, name, id_number, salary, department):
            self.salary = salary
            self.department = department
            Person.__init__(self, name, id_number)
a= Employee("John Pork", "12345", 50000, "Engineering")
a.display()