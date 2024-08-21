
"""
    Example to show Python does NOT support Method Overloading concept, like other
        programming languages like Java, C++ etc.

    Method overloading is a form of Polymorphism.

    Method overloading is the concept of having multiple functions with same name.
        Python will only register and recognize the last version of the function.
        In this example, it will remember add(a, b, c, d) version.

    So, in line #25, it will give below error -
        TypeError: add() missing 2 required positional arguments: 'c' and 'd'
"""

def add(a, b, c):
    return a + b + c

def add(a, b):
    return a + b

def add(a, b, c, d):
    return a + b + c + d

print(f"10 + 20 = {add(10, 20)}")
print(f"10 + 20 + 30 = {add(10, 20, 30)}")
print(f"10 + 20 + 30 + 40 = {add(10, 20, 30, 40)}")

