
# Import multiple libraries
import MyNumberLibrary as lib
import MyResultLibrary

sno = int(input("Enter Student Number: "))
sname = input("Enter Student Name: " )
marks1 = int(input("Enter marks in English: "))
marks2 = int(input("Enter marks in Science: "))
marks3 = int(input("Enter marks in Math: "))

total = lib.find_total(marks1, marks2, marks3)
print("Total marks are {}".format(total))
print("Average marks are {}".format(MyResultLibrary.find_average(total, 3)))
print("Result is {}".format(MyResultLibrary.find_result(marks1, marks2, marks3)))





