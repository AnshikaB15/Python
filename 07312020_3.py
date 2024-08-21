# Print reverse of the given number

# Ex: If input is 1234 ---> output should be 4321
# Ex: If input is 507 ----> output should be 705

def findReverse(no):
    rev = 0
    while no > 0:
        d = no % 10                 # Divide no by 10, and get remainder
        rev = (rev * 10) + d        # Whatever is in rev, multiply by 10, and then add d to it
        no = int(no / 10)           # Strip the digit that has been used (get integer part of the quotient when divided by 10)  

    return rev

no = int(input("Enter a number: " ))
reverse = findReverse(no)

print("Reverse of the given number is : " + str(reverse))

##############################################
#      no           d           rev   
#      ==           =           === 
#     123           3            0
#      12           2            3   
#       1           1           32
#       0                       321
##############################################
#      309          9            0
#       30          0            9
#        3          3           90
#        0                      903
################################################
