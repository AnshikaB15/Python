"""
    Parameters vs. Arguments

        Parameters are specified in the function definition.
        Arguments are specified during the function call.


        Parameters are nothing but local variables to the function.
"""

def get_PI():
    return 22 / 7

def find_area(r):                           # "r" is a parameter to this function
    return get_PI() * r * r

def find_circumference(radius):             # "radius" is a parameter to this function
    return 2 * get_PI() * radius

radius = float(input("Enter Radius of the Circle: "))
area = find_area(radius)                    # "radius" is an argument to the function call
circumference = find_circumference(radius)  # "radius" is an argument to the function call
print("Area: {} and Circumference: {}".format(area, circumference))


