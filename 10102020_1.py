"""
    Find the palindrome words in the given sentence.
	Ex:
		Input						Output
		=====						======
		MADAM SPEAKS MALAYALAM				MADAM
								MALAYALAM
"""
def findReverse(name):
    rev = ""                    # initialize the string with empty value
    
    for index in range(len(name) - 1, -1, -1):     # range(4, -1, -1)
        rev = rev + name[index]
        
    return rev

def isPalindrome(name):
    reverse = findReverse(name)     # Calling function
    return name == reverse

def printPalindromeWords(sentence):
    word = ""
    
    for ch in sentence:
        if ch != " ":
            word = word + ch
        else:
            if isPalindrome(word):      # Calling function
                print(word)
            word = ""

    if isPalindrome(word):          # This is exclusively for the last word
        print(word)

# Program execution starts here...
sentence = input("Enter a sentence: ")
printPalindromeWords(sentence)          # Calling function









