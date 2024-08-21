def findProductOfDigits(no):
    prod = 1

    # If the given number is negative, convert into it's positive value
    if no < 0:
        no = no * -1
    
    while no > 0:
        d = no % 10                 # Get last digit (divide by 10 and get remainder)
        prod = prod * d               # Add that digit to 'sum'    
        no = int(no / 10)           # Remove that digit (divide by 10 and get integer part of the quotient)

    return prod


no = int(input("Enter a number : "))
res = findProductOfDigits(no)
print("Sum of digits in {} is {}".format(no,findProductOfDigits(no)))

