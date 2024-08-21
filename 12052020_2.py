"""
    Example to demonstrate how we can do programming using the concept of Inheritence.
        In this example, we will have a Parent class, and 2 child classes.
        So, this is an example of Single Inheritence.

    In a company, there ar two types of employees - Full-time and Part-time.
        Full-time employees will have Id, Name, Salary. And, they will get 20% of bonus every year.
        Part-time employees will have Id, Name, hours_worked, rate_per_hour.
"""
class Employee:

    def __init__(self, id, name):
        self.id = id
        self.name = name

    def __str__(self):
        result = "\nEmployee Id: {}\nEmployee Name: {}".format(self.id, self.name)
        return result


# FullTimeEmployee is derived from the parent class 'Employee'
class FullTimeEmployee(Employee):

    def __init__(self, id, name, salary):
        super().__init__(id, name)          # Invokes __init__() of Employee class
        self.salary = salary

    def print_payment_details(self):
        bonus = self.salary * .20
        total_payment = self.salary + bonus
        print("\n{} will get a bonus of {}, and so, the total payment is {}".format(self.name, bonus, total_payment))

    def __str__(self):
        result = super().__str__() + "\nBasic Salary: {}".format(self.salary)
        return result

# PartTimeEmployee is derived from the base class 'Employee'
class PartTimeEmployee(Employee):

    def __init__(self, id, name, hours, rate):
        super().__init__(id, name)
        self.hours_worked = hours
        self.rate_per_hour = rate

    def print_payment_details(self):
        total_payment = self.hours_worked * self.rate_per_hour
        print("\n{} will get total payment of {}".format(self.name, total_payment))

    def __str__(self):
        result = super().__str__() + "\nHours worked: {}\nRate per hour: {}".format(self.hours_worked, self.rate_per_hour)
        return result

###################################################################################
emp1 = FullTimeEmployee(101, "John", 10000)
print(emp1)
emp1.print_payment_details()

emp2 = PartTimeEmployee(201, "Jack", 30, 20)
print(emp2)
emp2.print_payment_details()










