# Find total and average of given grades of a student

import ValidationsModule
import TotalCalculations as t, AverageCalculations as a

sno = int(input("Enter Student Number: "))
sname = input("Enter Student Name: ")
grade1 = int(input("Enter marks in English: "))
grade2 = int(input("Enter marks in History: "))
grade3 = int(input("Enter marks in Math: "))

ValidationsModule.doValidations(grade1, grade2, grade3)

total = t.getTotal(grade1, grade2, grade3)
avg = a.getAverage(grade1, grade2, grade3)

# print(sname + " has total of " + str(total) + " and average of " + str(avg))

output = "{} has total of {} and an average of {:.2f}"
print(output.format(sname, total, avg))

