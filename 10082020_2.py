"""
    Find whether the given string is a palindrome or not.
        A string is said to be palindrome, if it's reverse is similar to the string itself.

    Ex:
        MADAM
        RACECAR
        NOON
        MALAYALAM
        EVIL RATS ON NO STAR LIVE
        TACOCAT
        Able was I ere I saw Elba
"""

# Function to find reverse of the given string
def findReverse(name):
    rev = ""        # initialize the string with empty value
    
    for index in range(len(name) - 1, -1, -1):     # range(4, -1, -1)
        rev = rev + name[index]
        
    return rev

def isPalindrome(name):
    reverse = findReverse(name)     # Calling function
    return name == reverse
    
name = input("Enter your name: ")
if isPalindrome(name):          # Calling function
    print("Palindrome")
else:
    print("Not Palindrome")


    

