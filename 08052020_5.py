

# Multiplication Table

"""
    5 X 1 = 5
    5 X 2 = 10
    ....



    5 X 9 = 45
    5 X 10 = 50
"""

tableNo = int(input("Enter multiplication table: "))

for times in range(1, 11):
    print("{} X {} = {}".format(tableNo, times, (tableNo * times)))
          
