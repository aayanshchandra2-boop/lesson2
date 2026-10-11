from abc import ABC, abstractmethod


class absclass(ABC):
    def __init__(self, x):
        print("passed value is:", x)

    @abstractmethod
    def task(self):
        print("we are inside abstract class")


class test_class(absclass):
    def __init__(self, x=0):
        super().__init__(x)

    def task(self):
        print("we are inside test_class")


test_object = test_class(100)
test_object.task()