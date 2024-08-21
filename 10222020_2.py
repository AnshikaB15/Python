"""
   Global Variable Example.

       In this example, "x" is declared outside of any function; so it's a global variable.
           And, it can be accessed from anywhere in the program, including any function.
            
       We also have created a local variable 'x' in changeValue().
           So, in print() within the changeValue() -- it will access local variable.

        This is because whenever there is a clash between local and global variable, the function will always
            use local variable.
       
"""

x = 10

def changeValue():
    x = 20              # Creates a local variable
    print("Within changeValue() - {}".format(x))    # prints local variable
    
def printValue():
    print("Inside printValue() - {}".format(x)) # prints global variable
    
print("At start of the program - {}".format(x)) # prints global variable
x = 100         # change global variable
changeValue()
printValue()
print("At end of the program - {}".format(x))    # prints global variable



