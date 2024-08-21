
"""
    Example of "pass" keyword that can be used in a loop/function.
"""

def show_value(x):
    print("The current value is: {}".format(x))

def change_value(x):
    pass    # Used to indicate that Pythons should not look for statements in this function
    # TODO: Complete this section once the requirements are provided.

no = 100
show_value(no)
new_no = change_value(no)       # If the function does not return anything, new_no will get a value 'None'
print("Updated value is {}".format(new_no))


