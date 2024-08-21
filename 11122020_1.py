
# Examples of Functions

# Defining/Creating a function called 'find_total()'
def find_total(m1, m2, m3):     # m1, m2, m3 are parameters of the function
    return m1 + m2 + m3

# Defining/Creating a function called 'find_average()'
def find_average(m1, m2, m3):   # m1, m2, m3 are parameters of the function
    total = find_total(m1, m2, m3)  # Calling another function
    return total / 3

mEnglish = int(input("Enter marks in English: "))
mMath = int(input("Enter marks in Math: "))
mScience = int(input("Enter marks in Science: "))

# Calling find_total() function with Positional arguments
print("Total marks are {}".format(find_total(mEnglish, mMath, mScience)))

# Calling find_average() function with Keyword arguments
print("Average marks are {}".format(find_average(m2 = mMath, m3 = mScience, m1 = mEnglish)))  


      



