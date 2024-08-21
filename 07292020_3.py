# Find sum of the digits of the given number, using function
# 235 ---> 10
# 1908 ---> 18

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
print("Sum of digits of " + str(no) + " is : " + str(res))



#   no          d           sum
#   ==          =           ===
#   235         5            0
#    23         3            5
#     2         2            8
#     0                     10

# To get the digit --- I am doing % 10
# To remove the digit --- I am doing / 10, but get only integer part


