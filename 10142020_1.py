"""
    Program to find factorial of the given number.
        Ex:
            Input                 Output
            =====                 =======
             4                      24
             6                     720
             1                       1
             0                       1
"""
      
def factorial(no):
    if no == 0 or no == 1:
        return 1

    fact = 1
    for i in range(1, no + 1):
        fact = fact * i

    return fact
    

no = int(input("Please provide a positive integer: "))

if no < 0:
    print("Please provide a positive integer to continue....")
    exit()

print("Factorial of {} is {}".format(no, factorial(no)))

"""
        no     i       fact
        ==     =       ====
        4      1         1 
               2         1
               3         2
               4         6
               5         24 
"""
