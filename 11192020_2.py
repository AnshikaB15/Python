"""
    Example of creating our own class.
        And, creating objects from that class.

    In this example, the class is empty (does not hold any data or behavior).
"""

class Student:
    def __init__(self, sno, sname, scountry):   # 'self' refers to the current object
        self.id = sno           # 'id' is a property/attribute/field that holds data 
        self.name = sname       # 'name' is a property/attribute/field that holds data 
        self.country = scountry    # 'country' is a property/attribute/field that holds data

    # In the above function, 'sno', 'sname', 'scountry' are nothing but parameters; they are not stored on the object

    def show_values(x):
        print("Student ID is {}".format(x.id))
        print("Student Name is {}".format(x.name))
        print("Student Country is {}".format(x.country))
        
niti = Student(101, "Niti", "Canada")        # creates an object of Student class, and stores in 'niti' variable
print(type(niti))
print(niti)
niti.show_values()

print()
print()

rohan = Student(503, "Rohan", "USA")        # creates an object of Student class, and stores in 'rohan' variable
print(type(rohan))
print(rohan)            
rohan.show_values()




