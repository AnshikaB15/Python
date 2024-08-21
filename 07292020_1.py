
# Determine if the given number is odd or even, using a function

# We are defining a function named 'isEven()'
def isEven(x):
    return x % 2 == 0

no = int(input("Enter a number : "))

# We are calling the function
if(isEven(no)):
    print( str(no) + " is EVEN")
else:
    print(str(no) + " is ODD")


