"""
    Find whether the given number is Prime or not.
        A number is prime, if it is divisible by 1 and by itself.

    Ex:
        Input                Output
        =====                ======
          5                   Prime

          8                 Not Prime
"""

def checkPrimeOrNot(no):
    for i in range(2, no):
        if no % i == 0:
            print("{} is NOT Prime".format(no))
            exit()

    print("{} is Prime".format(no))

no = int(input("Enter a number: "))
checkPrimeOrNot(no)


"""
        no       i     rem         Output
        ==       =     ===         ====== 
        9        2      1
                 3      0        Not Prime
        
"""

