"""
    Default Parameter Value.
        If we don't provide a value for a parameter at time of calling the function, we can assign
            a default value for the missing parameter.
"""

def show(name, city = "Suspense"):
    print("{} is from {}".format(name, city))

show("Abbhijit", "Phoenix")
show("Anshul", "Atlanta")
show("Krishiv")
    # Normally, the above line would give an error. But since 'city' parameter has a default value in function definition,
    #   it is allowed (you are able to call a function with only 1 value, even though the function is defined to have 2 parameters.

