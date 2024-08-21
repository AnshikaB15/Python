"""
    Parameters vs. Arguments

        The number of parameters should be always equal to number of arguments.
        The first argument value will be stored in the first parameter variable, and so on.
            This is the usual style when we use 'Positional' Arguments.
        However, we can indicate which parameter is going to receive which argument, by using
            "key = value" format. "key" should be one of the parameters.
            This method is said to use 'Keyword Arguments'.        
"""


def sum(x, y, z):
    print("\nReceived values", "x = {}".format(x), "y = {}".format(y), "z = {}".format(z), sep="\t\t")
    total = x + y + z
    return total

print("Sum of 10, 20, 30 is {}".format(sum(10, 20, 30)))    # Positional Arguments
# print("Sum of 10, 20, 30 is {}".format(sum(10, 20)))        # Error 
# print("Sum of 10, 20, 30 is {}".format(sum(10, 20, 30, 40)))    # Error


print("Sum of 100, 200, 300 is {}".format(sum(y = 200, z = 300, x = 100)))   # Keyword Arguments    
# print("Sum of 100, 200, 300 is {}".format(sum(y = 200, z = 300, X = 100)))   # Error

