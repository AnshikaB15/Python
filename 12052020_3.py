"""
    Example of Multiple Inheritence.
        A child class inheriting from multiple parents.
"""

class First:

    def __init__(self, value):
        print("First.__init__()")
        self.x = value

    def __str__(self):
        print("First.__str__()")
        return str(self.x)

class Second:

    def __init__(self, value):
        print("Second.__init__()")
        self.y = value

    def __str__(self):
        print("Second.__str__()")
        return str(self.y)

# Child class inherits from First and Second classes
class Child(First, Second):

    def __init__(self, value1, value2, value3):
        print("Child.__init__()")
        super().__init__(value1)
        super().__init__(value2)
        self.z = value3

    def __str__(self):
        print("Child.__str__()")
        return super().__str__() + " " + super().__str__() + " " + str(self.z)

my_obj = Child(10, 20, 30)
print(my_obj)

