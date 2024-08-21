"""
    Find sum of digits in the given number.
        Ex:
            Input          Output
            =====          ======
             408             12
             -17              8
           -8908             25
               0              0 
"""

def findSumOfDigits(no):
    sum = 0

    # If the given number is negative, convert into it's positive value
    if no < 0:
        no = no * -1
    
    while no > 0:
        d = no % 10                 # Get last digit (divide by 10 and get remainder)
        sum = sum + d               # Add that digit to 'sum'    
        no = int(no / 10)           # Remove that digit (divide by 10 and get integer part of the quotient)

    return sum


no = int(input("Enter a number : "))
res = findSumOfDigits(no)
print("Sum of digits in {} is {}".format(no,findSumOfDigits(no)))

"""
    no       digit     sum
    ==       =====     ===
    156        6        0 
     15        5        6
      1        1       11 
      0                12
"""










