"""
    Example to demonstrate how we can do programming without using the concept of Inheritence.

    In a company, there ar two types of employees - Full-time and Part-time.
        Full-time employees will have Id, Name, Salary. And, they will get 20% of bonus every year.
        Part-time employees will have Id, Name, hours_worked, rate_per_hour.
"""
class FullTimeEmployee:

    def __init__(self, id, name, salary):
        self.id = id
        self.name = name
        self.salary = salary

    def print_payment_details(self):
        bonus = self.salary * .20
        total_payment = self.salary + bonus
        print("\n{} will get a bonus of {}, and so, the total payment is {}".format(self.name, bonus, total_payment))

    def __str__(self):
        result = "\nEmployee Id: {}\nEmployee Name: {}\nBasic Salary: {}".format(self.id, self.name, self.salary)
        return result

class PartTimeEmployee:

    def __init__(self, id, name, hours, rate):
        self.id = id
        self.name = name
        self.hours_worked = hours
        self.rate_per_hour = rate

    def print_payment_details(self):
        total_payment = self.hours_worked * self.rate_per_hour
        print("\n{} will get total payment of {}".format(self.name, total_payment))

    def __str__(self):
        result = "\nEmployee Id: {}\nEmployee Name: {}\nHours worked: {}\nRate per hour: {}".format(self.id, self.name, self.hours_worked, self.rate_per_hour)
        return result

emp1 = FullTimeEmployee(101, "John", 10000)
print(emp1)
emp1.print_payment_details()


emp2 = PartTimeEmployee(201, "Jack", 30, 20)
print(emp2)
emp2.print_payment_details()











