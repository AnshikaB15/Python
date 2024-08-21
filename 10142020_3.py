"""
    Find number of digits in the given number.
        Ex:
            Input          Output
            =====          ======
             408             3
             -17             2
           -8908             4
               0             1 
"""

def numberOfDigits(no):
    # If number is 0, returning 1 as the answer
    if no == 0:
        return 1

    # If no provided is negative, converting into positive value
    if no < 0:
        no = no * -1
    
    nDigits = 0
    while no > 0:
        nDigits = nDigits + 1
        no = int(no / 10)

    return nDigits

no = int(input("Enter a number: "))
print("Number of digits in {} is {}".format(no, numberOfDigits(no)))

"""
    no    nDigits
    ==    =======
    156      0 
     15      1
      1      2
      0      3
"""










