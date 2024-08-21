"""
    Program to find if the given string is a palindrome or not.

    Ex:
        hannah
        madam
        liril
        evil rats on no star live
        able was i ere i saw elba
"""

def isPalindrome(name):

    revOfName = name[::-1]
    return revOfName == name


name = input("Enter a string: " )
if(isPalindrome(name)):
    print("Given string is a palindrome")
else:
    print("Given string is not a palindrome")
