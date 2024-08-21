"""
    Find the palindrome words in the given sentence.
	Ex:
		Input						Output
		=====						======
		MADAM SPEAKS MALAYALAM				MADAM
								MALAYALAM
"""
def findReverse(word):
    rev = ""                    # initialize the string with empty value
    
    for index in range(len(word) - 1, -1, -1):     # range(4, -1, -1)
        rev = rev + word[index]
        
    return rev

def isPalindrome(word):
    if len(word) == 1:                      # Avoiding single letter words
        return False
        
    reverse = findReverse(word)              # Calling function
    return word == reverse

def printPalindromeWords(sentence):
    word = ""
    
    for ch in sentence:
        if ch != " ":
            word = word + ch
        else:
            if isPalindrome(word):            # Calling function
                print(word)
            word = ""

# Program execution starts here...
sentence = input("Enter a sentence: ")
printPalindromeWords(sentence.upper() + " ")          # Calling function
"""
        Transforming the sentence into Upper case, so that if the user
            gives the value in mixed case also, it will work.
        You can use lower() as well.
        
         Adding space will ensure that the last word is also considered in the logic".
"""      








