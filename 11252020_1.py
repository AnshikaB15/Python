"""
    Example of a class with -
        (a) __init__ ---> constructor / initialization method
        (b) Total 6 attributes, 3 of which are created in __init__, and, 3 in calculate_net()
        (c) Total 3 methods aka functions, among which 1 is having a pre-defined name "__init__()"
        (d) __init__() is called only once in this program, because we are creating only 1 object
        (e) Documentation String that the programmer can write to explain the objective of the class.
                This is any string written immediately after "class".
                We can access the documentation string using __doc__ attribute, on an object, or, directly on a class.
        (f) Class variable "employee_count"
"""

class Employee:
    # Documentation String
    "Class holding data and behavior of Employee objects"

    # Class variables
    employee_count = 0
    
    # Constructor / Initialization Method
    def __init__(self, id, name, basic):
        self.eno = id
        self.ename = name
        self.basic = basic
        Employee.employee_count += 1      # we have to access class variable using the Class name

    # This method creates 3 attributes on the Class
    def calculate_net(self):
        self.tax = self.basic * .20         # tax is 20% of basic salary
        self.bonus = self.basic * .10       # bonus is 10% of basic salary 
        self.net = self.basic + self.bonus - self.tax

    def print_result(self):
        print()
        print("Employee Number is {}".format(self.eno))
        print("Employee Name is {}".format(self.ename))
        print("Employee Basic Salary is {}".format(self.basic))
        print("Tax is {}".format(self.tax))
        print("Bonus is {}".format(self.bonus))
        print("Net Salary is {}".format(self.net))
        print()

no = int(input("Enter Employee Number: "))
name = input("Enter Employee Name: ")
sal = int(input("Enter Employee's Basic Salary: "))

e1 = Employee(no, name, sal)
e1.calculate_net()
e1.print_result()

e2 = Employee(1000, "Ram", 10000)
e2.calculate_net()
e2.print_result()


print(e1.__doc__)       # Prints the documentation string if present, or, None
print(Employee.__doc__) # Prints the documentation string if present, or, None

print("Total number of employees present are: {}".format(Employee.employee_count))
