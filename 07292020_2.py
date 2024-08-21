# Factorial of given number

def findFactorial(no):
    x = 1
    res = 1
    
    while x <= no:
        res = x * res
        x = x + 1

    return res

no = int(input("Enter a number : "))
result = findFactorial(no)
print(str(no) + " != " + str(result))

# 5  ----> 1 * 2 * 3 * 4 * 5
# 3 -----> 1 * 2 * 3

#   no         x        res     
#   ==         =        ===
#   5          1         1 
#              2         1
#              3         2
#              4         6
#              5        24
#              6       120
