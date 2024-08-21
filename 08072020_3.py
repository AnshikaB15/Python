"""
    Fibonacci Series Program.
    0 1 1 2 3 5 8 .....

    
"""

noOfTerms = int(input("Enter no. of terms you want in the Series: "))

if noOfTerms <= 2:
    print("Please provide a value more than 2...")
    exit()

term1 = 0
term2 = 1
print(term1)
print(term2)

for termNumber in range(3, noOfTerms + 1):
    term3 = term1 + term2
    print(term3)

    term1 = term2
    term2 = term3

"""
    term1      0   1    1 
    term2      1   1    2
    term3      1   2    3
"""



