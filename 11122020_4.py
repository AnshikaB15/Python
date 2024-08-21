
# Example for Arbitrary Keyword Arguments

def print_names(**values):
    print()
    print("Total number of values received {}".format(len(values)))
    print("Type of values received {}".format(type(values)))

    # Loop the dictionary
    for entry in values.items():
        print(entry)

print_names(IL = "Chicago", AZ = "Phoenix")
print_names(USA = "DC", Canada = "Ottawa", France = "Paris", Russia = "Moscow")
