
"""
    Program to print reverse of the given number.
        Ex:
            Input        Output
            =====        ======
              259          952
             -109         -901 
"""

def reverse(no):
    if no < 0:
        no = no * -1

    rev = 0
    while no > 0:
        digit = no % 10
        rev = (rev * 10) + digit
        no = int(no / 10)

    return rev

no = int(input("Enter a Number: "))
if no < 0:
    print("Reverse of {} is -{}".format(no, reverse(no)))
else:
    print("Reverse of {} is {}".format(no, reverse(no)))
    
"""
        no    digit      rev
        ==    =====      ===
       123      3         0
        12      2         3
         1      1        32
         0              321
"""
