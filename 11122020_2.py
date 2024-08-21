
# Example for Arbitrary Arguments

def print_values(*args):
    print()
    print("Total number of values received {}".format(len(args)))
    print("Type of the values received {}".format(type(args)))
    print("First value received {}".format(args[0]))

    # Print/Loop all values received
    for value in args:
        print(value)

print_values("Chicago", "Phoenix", "Toronto")
print_values(10, 20, 30, 40, 50)




