"""
    Find mean of a given group of values.
        Mean is nothing but average of the values.
        Mean = Sum of Values
               -------------
               No. of Values
"""
count = int(input("Enter how many values you want to provide: "))

# Create empty list to hold the values going to be given by the user
values = []

# Accept values from the user
for i in range(0, count):
    values.append(int(input("Enter value for {} element: ".format(i + 1))))

print("You gave me this list of values: {}".format(values))

# Find Mean
sum = 0
for value in values:
    sum += value       # sum = sum + value

mean = sum / len(values)
print("Mean is {:.2F}".format(mean))

"""
    count     values       i       value        sum        mean
    =====     ======       =       =====        ===        ====
      3         []         0
               [10]        1
              [10, 20]     2
            [10, 20, 30]        
                                     10          0
                                     20         10
                                     30         30
                                                60
                                                            20.0

"""





