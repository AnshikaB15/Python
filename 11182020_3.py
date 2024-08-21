
"""
    Factorial using Recurion.
        Factorial of 5 = 1 * 2 * 3 * 4 * 5 = 120

        factorial(5) = 5 * factorial(4)
        factorial(4) = 4 * factorial(3)
        factorial(3) = 3 * factorial(2)
        factorial(2) = 2 * factorial(1)
        factorial(1) = 1
        
"""

def factorial(no):
    if no > 1:
        return no * factorial(no - 1)   # Recursive function call
    else:
        return 1

no = int(input("Enter a number: "))
fact = factorial(no)
print("{}! = {}".format(no, fact))

"""
    https://cdn.programiz.com/sites/tutorial2program/files/cpp-function-recursion-example.png
"""
