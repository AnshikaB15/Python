

"""
    Print all the characters of the given string, in reverse.
"""
name = input("Enter your name: ")
print()

# Solution using 'for' loop
for index in range(len(name) - 1, -1, -1):   
    print(name[index])

"""
    The reasons behind having three -1s in the loop -
        1. First one - is to get the last index of the string (which is total characters - 1)
        2. Second one - is to make the for loop go until the value becomes -1; which means it will go until 0.
        3. Third one - is step value; and we want it to go 1 character in reverse

"""



"""
Python
    len("Python") ----- 6
    
    name[5]
    name[4]
    name[3]
    name[2]
    name[1]
    name[0]

White House

    len("White House") ---- 11

    name[10]
    name[9]
    ....
    ....
    name[1]
    name[0]

"""
