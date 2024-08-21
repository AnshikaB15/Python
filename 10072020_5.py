

"""
    Find the length of your name, without using built-in function len()
"""

name = input("Enter your name: ")

counter = 0
for ch in name:
    counter = counter + 1

print("Length of {} is {}".format(name, counter))

