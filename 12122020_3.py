"""
    Example to show how we can implement Method Overloading in Python.
        For this, we use 'multipledispatch' module.

        Get the module - "pip install multipledispatch"
"""

from multipledispatch import dispatch

@dispatch(int, int, int)
def add(a, b, c):
    return a + b + c

@dispatch(int, int)
def add(a, b):
    return a + b

@dispatch(int, int, int, int)
def add(a, b, c, d):
    return a + b + c + d

@dispatch(float, float)
def add(a, b):
    return a + b

print(f"10 + 20 = {add(10, 20)}")
print(f"10 + 20 + 30 = {add(10, 20, 30)}")
print(f"10 + 20 + 30 + 40 = {add(10, 20, 30, 40)}")
print(f"10.5 + 20.5 = {add(10.5, 20.5)}")
