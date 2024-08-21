"""
    Program to print Fibonacci series for given n term.
        The minimum terms should be 2.
        
        Fibonacci series starts with two terms 0 and 1.
            Any other term in the series is sum of previous two terms.

        Ex:
            0
            1
            1
            2
            3
            5
            8
            13
            21
            ....
            ....
"""

def printFibonacciSeries(n):
    term1 = 0
    term2 = 1
    print(term1)
    print(term2)

    for i in range(3, n + 1):
        nextTerm = term1 + term2
        print(nextTerm)

        term1 = term2
        term2 = nextTerm

n = int(input("Enter number of terms that you want in the Fibonacci series..."))

if n < 2:
    print("You will get at the minimum 2 terms...")
    exit()

printFibonacciSeries(n)    

"""
    n    i      term1      term2        nextTerm
    =    =      =====      =====        ========= 
    6    3        0          1             1
         4        1          1             2
         5        1          2             3 
         6        2          3             5
         7

"""


