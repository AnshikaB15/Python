# Handling the scenario, based on the exact exception that occurred.

print("Welcome to my Division Program!")

while True:
    try:
        print()
        n1 = int(input("Enter Numerator for Division: "))
        n2 = int(input("Enter Denominator for Division: "))

        quotient = n1 / n2
        remainder = n1 % n2
        
    except ValueError:
         print("Please provide INTs only for Numerator and Denominator")

    except ZeroDivisionError:
        print("Please provide a Non-Zero INT for Denominator")

    except Exception as e:
        print("Some other exception occurred: ", e.__class__)

    else:
        print("Quotient is ", quotient)
        print("Remainder is ", remainder)

    finally:
        print()
        choice = input("Do you want to try one more time - Y/N: ")
        if choice != 'Y' and choice != 'y':
            break

print("\nThanks for using my Division Program!")
