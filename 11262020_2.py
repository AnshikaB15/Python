# Example of inter-object relationships

class Department:
    def __init__(self, no, name, location):
        self.dno = no
        self.dname = name
        self.location = location
        self.employees = []     # An empty list is created for 'employees' attribute in every object of Department class

    def __str__(self):
        return "Department {} is based out of {}, and its employees are {}".format(self.dname, self.location, self.get_employees())

    def get_employees(self):
        result = "\n"
        for emp in self.employees:
            result = result + "\t" + str(emp) + "\n"        # str(emp) will invoke __str__() of Employee class
        return result

    def add_employee(self, emp):
        self.employees.append(emp)

class Employee:
    def __init__(self, id, name, salary):
        self.eid = id
        self.ename = name
        self.basic = salary

    def __str__(self):
        return "{} has ID {} and Salary of {}".format(self.ename, self.eid, self.basic)

anshul = Employee(100, "Anshul", 10000)
krishiv = Employee(200, "Krishiv", 10000)
abbhijit = Employee(150, "Abbhijit", 12000)

mktg = Department(10, "Marketing", "Miami")
mktg.add_employee(anshul)
mktg.add_employee(krishiv)

finance = Department(20, "Finance", "SFO")
finance.add_employee(abbhijit)

print(mktg)
print(finance)














