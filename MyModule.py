

def is_odd(no):
    try:
        if no % 2 == 1:
            return True
        else:
            return False

    except TypeError:
        raise Exception("Please provide an integer only...")

    
