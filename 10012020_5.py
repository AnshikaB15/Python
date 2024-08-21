"""
    Print odd numbers using functions.
"""

# Definition of functions.
def isOdd(no):                      # 'no' is the argument of the function
    return no % 2 == 1

def printOddNumbers(start, end):    # 'start' and 'end' are arguments of the function
    print()
    print("Printing all Odd Numbers between {} and {}".format(start, end))
    while start <= end:
        if isOdd(start):            # Calling 'isOdd()' from here.
            print(start)
        start = start + 1

print("Welcome to my program of finding the odd numbers")
print("================================================")

x = int(input("Enter starting value: "))
y = int(input("Enter ending value: "))

printOddNumbers(x, y)                       # Calling the function with values present in 'x' and 'y' variables





