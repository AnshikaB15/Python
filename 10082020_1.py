"""
    Print the given name in reverse.
        Ex: If input is "Python", output should be "nohtyP"
"""

# Function to find reverse of the given string
def findReverse(name):
    rev = ""        # initialize the string with empty value
    
    for index in range(len(name) - 1, -1, -1):     # range(4, -1, -1)
        rev = rev + name[index]
        
    return rev

name = input("Enter your name: ")
reverse = findReverse(name)     # Calling the function with 1 parameter
print("Reverse of {} is {}".format(name, reverse))



"""
    name     index    name[index]      rev
    ====     =====    ==========       === 
    India      4           a            a
               3           i            ai
               2           d            aid
               1           n            aidn
               0           I            aidnI
"""
