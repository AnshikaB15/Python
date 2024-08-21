
# Example for Arbitrary arguments

def add(*values):
    sum = 0
    
    for value in values:
        sum += value

    return sum

print("Addition result is {}".format(add(10, 20, 30)))
print("Addition result is {}".format(add(10, 20, 30, 40, 50)))
print("Addition result is {}".format(add(10, 20)))
print("Addition result is {}".format(add(10, 20, 30, 40, 50, 60)))
print("Addition result is {}".format(add(10)))
