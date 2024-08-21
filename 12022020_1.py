
print("Welcome to my Division Program!")

while True:
    try:
        print()
        n1 = int(input("Enter Numerator for Division: "))
        n2 = int(input("Enter Denominator for Division: "))

        quotient = n1 / n2
        remainder = n1 % n2
        
    except:
         print("Please provide proper values...")       

    else:
        print("Quotient is ", quotient)
        print("Remainder is ", remainder)

    finally:
        print()
        choice = input("Do you want to try one more time - Y/N: ")
        if choice != 'Y':
            break

print("\nThanks for using my Division Program!")
