"""
    Local vs. Global variables.

"""

def change_1():
    x = 100                     # This creates a local variable x
    y = 200                     # This creats a local variable y
    print("At end of change_1() --- x = {} and y = {}".format(x, y))    # access local variables

def print_1():
    print("Inside print_1() -- x = {} and y = {}".format(x, y))         # accessing global variables
    sum = x + y                             # creates a local variable 'sum' that can be used only in this function
    print("Sum is {}".format(sum))
    
def change_2():
    global x, y                 # gets access to global variables x and y
    x = 1000                    # updates global variable x
    y = 2000                    # updates global variable y
    print("At end of change_2() --- x = {} and y = {}".format(x, y))

def change_3():
    global y                    # gets access to global variable y  
    x = -100                    # creates local variable x
    y = -200                    # updates global variable y
    print("At end of change_2() --- x = {} and y = {}".format(x, y))    

x = 10
y = 20

print("At start of the program x = {} and y = {}".format(x, y)) # access global variables
print_1()
change_1()
print("In middle of the program x = {} and y = {}".format(x, y))   # access global variables
change_2()
print("Almost at end the program x = {} and y = {}".format(x, y))   # access global variables
change_3()
print("At end of the program x = {} and y = {}".format(x, y))   # access global variables
