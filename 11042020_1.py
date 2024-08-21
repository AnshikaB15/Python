"""
    Example for "else" in the while/for loops
"""

print("Program starts...")

x = 1
while x <= 5:
    print(x)
    x = x + 1
else:
    print("This is the end of the loop...")

print("While loop example ends....")

for x in range(11, 16):
    print(x)
else:
    print("The for loop also ended...")
    
print("For loop example ends...")
print("Program ends...")


