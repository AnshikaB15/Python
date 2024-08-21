"""
    Print all the factors of the given number.
        A factor is a number that divides into another number exactly and without leaving a remainder.

    Ex:
        Input                Output
        =====                ======
          5                    1
                               5

          8                    1
                               2
                               4
                               8
"""

def printFactors(no):
    if no <= 0:
        print("Please provide a number which is greater than zero")
        exit()
    
    for i in range(1, no + 1):
        if no % i == 0:
            print(i)

no = int(input("Enter a number: "))
printFactors(no)

"""
        no       i     rem     Output
        ==       =     ===     ======
        6        1      0        1
                 2      0        2
                 3      0        3
                 4      2       
                 5      1
                 6      0        6
                 7
"""

