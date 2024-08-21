"""
    Print Odd Numbers between 1 and 10, using 'for' loop, but without providing
        the step value.
"""

print("Program starts here....")

for no in range(1, 11):
    rem = no % 2
    if rem == 1:
        print(no)

print("Program ends here.....")
