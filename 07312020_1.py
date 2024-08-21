# Printing factors of the given number, using function

# If input is 6 ---> Output should be 1 2 3 6
# If input is 9 ---> output should be 1 3 9
# If input is 17 --> ouput should be 1 17

def printFactors(no):
    x = 1
    
    while x <= no:
        if no % x == 0:
            print(x)

        x = x + 1

no = int(input("Enter a number: "))
printFactors(no)


########################################################
#  no       x
#  ==       =
#   6       1       ----> Print x value ---> 1
#           2       ----> Print x value ---> 2
#           3       ----> Print x value ---> 3
#           4       
#           5
#           6       ----> Print x value ---> 6
#           7
##########################################################
#   4       1       ----> 1 is printed
#           2       ----> 2 is printed  
#           3
#           4       ----> 4 is printed
#           5
#
#




