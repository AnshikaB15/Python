
"""
    Module having multiple functions.
"""

def checkSignStatus(no):
    if no < 0:
        print("{} is negative".format(no))
    elif no > 0:
        print("{} is positive".format(no))
    else:
        print("{} is Zero".format(no))


def isOdd(no):
    return no % 2 == 1


def find_total(m1, m2, m3):
    return m1 + m2 + m3


