"""
    Sum of Digits using Recursion.
        123 = 1 + 2 + 3 = 6

        sumOfDigits(123) = 3 + sumOfDigits(12)
        sumOfDigits(12)  = 2 + sumOfDigits(1)
        sumOfDigits(1)   = 1 + sumOfDigits(0)
        sumOfDigits(0)   = 0
"""

def sumOfDigits(no):
    if no == 0:
        return 0
    else:
        return (no % 10) + sumOfDigits(int(no / 10))

no = int(input("Enter a number: "))
sum = sumOfDigits(no)
print("Sum of Digits of {} = {}".format(no, sum))
