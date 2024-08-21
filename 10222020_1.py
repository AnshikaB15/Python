"""
   Global Variable Example.

       In this example, "x" is declared outside of any function; so it's a global variable.
           And, it can be accessed from anywhere in the program, including any function.
            
        In this example, both changeValue() and printValue() functions are accessing the global
            variable 'x'. This is possible by using 'global' keyword.

        What happens if the functions don't use 'global' keyword?

"""

x = 10

def showValue():
    print("At start of the changeValue() - {}".format(x)) # Prints global variable
    
def printValue():
    print("Inside printValue() - {}".format(x))     # Prints global variable
    
print("At start of the program - {}".format(x))     # Prints global variable
x = 100
showValue()
printValue()        
print("At end of the program - {}".format(x))       # Prints global variable



