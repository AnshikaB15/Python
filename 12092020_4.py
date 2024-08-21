
# Processing student records present in a data file (values separated by comma)

import csv

print("Processing of Student records - BEGIN....")

with open("C:\\Users\\Sreeram\\Documents\\Student_Data.dat", "r") as students:
    reader = csv.reader(students, delimiter=",")

    for student in reader:
        total = int(student[3]) + int(student[4]) + int(student[5])
        print(student[1], " studying in Grade: ", student[2], " has a total marks of ", total)

print("Processing of Student records - END....")



""""
    Student_Data.dat will have content like below ---
        101,Anshul,7,100,80,60
        102,Abbhijit,12,100,90,70
        103,Krishiv,8,90,80,100
        104,Rohan,7,90,90,80
""""
