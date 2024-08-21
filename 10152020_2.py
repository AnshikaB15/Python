"""
    Find whether the given number is Prime or not.
        A number is prime, if it is divisible by 1 and by itself.

    Ex:
        Input                Output
        =====                ======
          5                   Prime

          8                 Not Prime
"""

def isPrime(no):
    count = 0

    for i in range(1, no + 1):
        if no % i == 0:
            count = count + 1

    if count == 2:
        return True
    else:
        return False

no = int(input("Enter a number: "))
if isPrime(no):
    print("{} is Prime".format(no))
else:
    print("{} is not Prime".format(no))


"""
        no       i     rem     count     Output
        ==       =     ===     =====     ====== 
        6        1      0        0      Not Prime     
                 2      0        1
                 3      0        2
                 4      2        3
                 5      1        4
                 6      0        
                 7

        9        2      1
                 3      0               Not Prime
        
"""

