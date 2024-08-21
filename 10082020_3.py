"""
    Print each word of the given sentence in a separate line.

    Ex:
        Input ---> Python is an easy language to learn
        Output --->
                        Python
                        is
                        an
                        easy
                        language
                        to
                        learn
"""

def printWords(name):
    word = ""
    
    for ch in name:
        if ch != " ":
            word = word + ch
        else:
            print(word)         # prints all words except for the last word
            word = ""

    print(word)                 # for printing the last word

name = input("Enter your name: ")
printWords(name)

"""
    name      ch       word        output  
    ====      ==       ====        ======
   Tom Cat             blank 
              T        T 
              o        To
              m        Tom
           space                    Tom
                       blank
              C        C
              a        Ca
              t        Cat
                                    Cat
"""

