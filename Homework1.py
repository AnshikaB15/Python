




def findReverse(word):
    rev = ""                    # initialize the string with empty value
    
    for index in range(len(word) - 1, -1, -1):     # range(4, -1, -1)
        rev = rev + word[index]
        
    return rev

def isPalindrome(word):
    reverse = findReverse(word)     # Calling function
    return word == reverse

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

