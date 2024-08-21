# Input two numbers. Print all even numbers between the two numbers.
# If you give 1 and 10, it will print 2 4 6 8 10
# If you give 10 and 1, it will print 10 8 6 4 2
# If you give 10 and 10, it will print 10
# If you give 5 and 5, it will print NOTHING

start = int(input("Enter first number: "))
end = int(input("Enter second number: "))

if start < end:
    while start <= end:
        if start %  2 == 0:
            print(start)

        start = start + 1
else:
    while start >= end:
        if start % 2 == 0:
            print(start)

        start = start - 1


        
    
    
