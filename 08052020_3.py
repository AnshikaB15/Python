"""
    Input your full name.

    Find -
        (1) No of upper case characters
        (2) No of lower case characters
        (3) No of digits
        (4) No of other characters.

    Ex:
        "James Bond 007"  ---> 2, 7, 3, 2


    We have to use ASCII values to identify whether a character is upper case, lower case etc
        (American Standard Code for Information Interchange)

    65 - 90 are for Upper case
    97 - 122 are for Lower case
    48 - 57 are for Digits.

    To find the ASCII value of any character, we have to use ord()
"""

name = input("Enter your full name: ")

noDigits = 0
noUC = 0
noLC = 0
noOther = 0 

for letter in name:
    asciiValue = ord(letter)

    if asciiValue >= 65 and asciiValue <= 90:
        noUC = noUC + 1
    elif asciiValue >= 97 and asciiValue <= 122:
        noLC = noLC + 1
    elif asciiValue >= 48 and asciiValue <= 57:
        noDigits = noDigits + 1
    else:
        noOther = noOther + 1

print("No of Upper case characters are {}".format(noUC))
print("No of Lower case characters are {}".format(noLC))
print("No of Digits are {}".format(noDigits))
print("No of Other characters are {}".format(noOther))


        

















