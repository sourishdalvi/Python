from abc import ABC, abstractmethod
class AbstractClass(ABC):
    def print(self, x):
        print("Passed value: ", x)
    @abstractmethod   
    def task(self):
        print("we are in abstract class task")
class test_class(AbstractClass):
    def task(self):
        print("we are in test class task")
test_object = test_class()
test_object.task()
test_object.print(100)  