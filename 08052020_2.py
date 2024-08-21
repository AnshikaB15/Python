
"""
Input 2 numbers, and find sum of odd, sum of even of all numbers that exist
between the two given numbers.

    Ex: 1 and 5 ---> 1 + 3 + 5 = 9
                        2 + 4 = 6
"""

start = int(input("Enter starting number: "))
end = int(input("Enter ending number: "))

sumOdd = 0
sumEven = 0

for no in range(start, end + 1):
    if(no % 2 == 1):
        sumOdd = sumOdd + no
    else:
        sumEven = sumEven + no

print("Sum of odd numbers is {}".format(sumOdd))
print("Sum of even numbers is {}".format(sumEven))


