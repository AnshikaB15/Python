"""
    Example for "break" and "continue" in the while/for loops
"""

print("Program starts...")

count = 1
while count <= 10:
    if count > 5:
        break
    
    print(count)
    count += 1      # count = count + 1
else:
    print("While loop ended here....")      # This is not executed, because we are 'break'ing from the loop

print("while ended, for started.....")

for x in range(11, 20):
    if x % 2 == 0:
        break

    print(x)
else:
    print("While loop ended here....")      # This is not executed, because we are 'break'ing from the loop

print("Program ends....")
    


