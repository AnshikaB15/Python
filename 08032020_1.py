# Find total and average of given grades of a student

sno = int(input("Enter Student Number: "))
sname = input("Enter Student Name: ")
grade1 = int(input("Enter marks in English: "))
grade2 = int(input("Enter marks in History: "))
grade3 = int(input("Enter marks in Math: "))

if(grade1 < 0 or grade1 > 100):
    print("Please provide 0 to 100 only")
    exit()

if(grade2 < 0 or grade2 > 100):
    print("Please provide 0 to 100 only")
    exit()

if(grade3 < 0 or grade3 > 100):
    print("Please provide 0 to 100 only")
    exit()

total = grade1 + grade2 + grade3
avg = total / 3

# print(sname + " has total of " + str(total) + " and average of " + str(avg))

output = "{} has total of {} and an average of {:.2f}"
print(output.format(sname, total, avg))

