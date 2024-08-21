"""
    Example for "break" and "continue" in the while/for loops
"""

print("Program starts...")

count = 1
while count <= 10:
    print(count)
    count += 1      # count = count + 1
    
    if count == 5:
        continue        # This makes the control to go line #8 (skips below part of the loop)
    elif count > 5:
        break           # This makes the control to go to line #19 (skips below part of the loop)    

    print("Iteration of while loop done..")

print("while ended, for started.....")

for x in range(11, 20):
    print(x)
    
    if x % 2 == 0:
        continue
    elif x % 3 == 0:
        break

    print("Iteration of for loop done...")

print("Program ends....")
    


