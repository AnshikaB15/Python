"""
 Input your name. Print each word in a separate line.
	Ex:  James Bond 007 -----> James
				   Bond
				   007
	
"""

name = input("Enter your name: ")

word = ""
for letter in name:
    if letter == " ":
        print(word)
    else:
        word = word + letter

print(word)
