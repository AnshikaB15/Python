"""
    Examples of 'for' loop.
"""

# Print Numbers for 1 to 10
print("Numbers from 1 to 10..")
print("======================")
for no in range(1, 11):     # no starts with 1, step value +1, until no is 10
    print(no)

# Print Odd Numbers from 1 to 10 ---- 1, 3, 5, 7, 9
print()
print("Odd Numbers from 1 to 10..")
print("==========================")
for no in range(1, 11, 2):  # no starts with 1, step value +2, until no is 10
    print(no)

# Print Numbers from 1 to 10 in reverse
print()
print("Numbers from 10 to 1..")
print("=======================")
for no in range(10, 0, -1): # no starts with 10, step value -1, until no is 1
    print(no)

# Print Even Numbers from -10 to +10 in reverse
print()
print("Even Numbers from 10 to -10..")
print("=============================")
for no in range(10, -11, -2): # no starts with 10, step value -2, until no is -10
    print(no)

# Numbers between 1 and 10.
print()
print("Numbers from 1 to 10")
print("====================")
for no in range(10):        # no starts with 0, each time +1, goes until 9
    print(no + 1)
