
"""
    Example of a function calling another function.
        find_average() is calling find_total()
    And, we are calling find_average() from the main part of the program.
"""

def find_total(x, y, z):
    return x + y + z

def find_average(m1, m2, m3):
    total = find_total(m1, m2, m3)
    return total / 3

marks1 = int(input("Enter Marks in Math: "))
marks2 = int(input("Enter Marks in English: "))
marks3 = int(input("Enter Marks in Science: "))

average = find_average(marks1, marks2, marks3)
print("Average marks are {}".format(average))
