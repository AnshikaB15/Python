
"""
    
        Factorial of 5 = 1 * 2 * 3 * 4 * 5 = 120
        
"""

def factorial(no):
    result = 1
    
    for i in range(1, no+1):
        result = result * i

    return result



no = int(input("Enter a number: "))
fact = factorial(no)
print("{}! = {}".format(no, fact))

"""
result          i       no      fact
======          =       ==      ====
   1            1        4
   1            2
   2            3
   6            4
  24                              24
"""
