"""
    Class that has examples for -
        (a) Constructor ----> __init__()
        (b) Destructor  ----> __del__()
        (c) Delete object's property  ----> del object.property_name
        (d) Delete object itself      ----> del object
        (e) Converting object into string ---> __str__()
        (f) Represenation of an object    ---> __repr__()
"""

class Student:
    "Class responsible to handle Student details"
    
    count = 0       # class variable

    def __init__(self, no, name):
        self.sno = no
        self.sname = name
        Student.count += 1

    def __del__(self):
        Student.count -= 1

    def store_marks(self, m1, m2, m3):
        self.mEnglish = m1
        self.mMath = m2
        self.mScience = m3

    def find_total(self):
        self.total = self.mEnglish + self.mMath + self.mScience

    def find_average(self):
        self.avg = self.total / 3

    def find_result(self):
        if self.avg >= 90:
            self.result = 'A'
        elif self.avg >= 80:
            self.result = 'B'
        elif self.avg >= 60:
            self.result = 'C'
        else:
            self.result = 'D'

    def print_results(self):
        print()
        print("Student ID is {}".format(self.sno))
        print("Student Name is {}".format(self.sname))
        print("Student Total is {}".format(self.total))
        print("Student Average is {}".format(self.avg))
        print("Student Result is {}".format(self.result))
        print()

    def __str__(self):
        return "{} has ID of {} and result as {}".format(self.sname, self.sno, self.result)

    def __repr__(self):
        return "{} : {} : {} : {} : {}".format(self.sno, self.sname, self.total, self.avg, self.result)

    
anshika = Student(100, "Anshika")
anshika.store_marks(80, 90, 100)
anshika.find_total()
anshika.find_average()
anshika.find_result()
anshika.print_results()

devan = Student(200, "Devan")
devan.store_marks(95, 85, 90)
devan.find_total()
devan.find_average()
devan.find_result()
devan.print_results()

print("Total number of students are {}".format(Student.count))

print(anshika)

del anshika.result              # this deletes 'result' attribute from 'anshika' object
devan.print_results()
# anshika.print_results()       # this will give error, because print_results() tries to access 'result' property which is no longer present

del devan                       # deletes 'devan' object itself
# devan.print_results()           # this will give error, because 'devan' object itself has been deleted.

print("Total number of students are {}".format(Student.count))






