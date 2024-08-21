"""
    Find the acronym of the given sentence.
	Dis-regard words "of", "the", "and".
	
	Ex: 
		Input					Output
		=====					======
		United States of America 		 USA
		World Health Organization		 WHO
"""

def printAcronym(sentence):
    word = ""
    acronym = ""
    
    for ch in sentence:
        if ch != " ":
            word = word + ch
        else:
            if word != "OF" and word != "THE" and word != "AND":
                acronym = acronym + word[0]
            word = ""

    print("Acronym of {}is {}".format(sentence, acronym))
            
# Program execution starts here...
sentence = input("Enter a sentence: ")
printAcronym(sentence.upper() + " ")          # Calling function
