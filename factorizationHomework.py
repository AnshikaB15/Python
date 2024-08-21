def findProductOfDigits(no):
    product = 1

    
    if no < 0:
        no = no * -1
    
    while no > 0:
        d = no % 10                 
        product = product * d
        no = int(no / 10)          

    return product


no = int(input("Enter a number : "))
res = findProductOfDigits(no)
print("Product of digits of " + str(no) + " is : " + str(res))
