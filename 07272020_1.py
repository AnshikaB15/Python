# Get Marks in 5 subjects, and decide the result (Pass/Promoted/Fail)
# PASS is when the student gets at least 50 marks in all the 5 subjects
# PROMOTED is when the student gets at least 50 marks in at least 3 subjects
# FAIL in other cases

# 70 50 90 55 60 ----> Pass
# 60 70 90 40 80 ----> Promoted
# 40 90 80 48 70 ----> Promoted
# 40 90 30 20 90 ----> Fail

name = input("Enter your name : ")
m1 = int(input("Enter marks in Subject 1 : "))
m2 = int(input("Enter marks in Subject 2 : "))
m3 = int(input("Enter marks in Subject 3 : "))
m4 = int(input("Enter marks in Subject 4 : "))
m5 = int(input("Enter marks in Subject 5 : "))

# Example of NESTED IF (IF within another IF)

if m1 >= 50:
    if m2 >= 50:
        if m3 >= 50:
            if m4 >= 50:
                if m5 >= 50:
                    print("Result is PASS")
                else:
                    print("Result is PROMOTED")
            else:
                print("Result is PROMOTED")
        else:
            if m4 >= 50:
                print("Result is PROMOTED")
            else:
                if m5 >= 50:
                    print("Result is PROMOTED")
                else:
                    print("Result is FAIL")
    else:
        print("Result is PROMOTED")
        else:
            if m4 >= 50:
                print("Result is PROMOTED")
             else:
                 if m5 >= 50:
                   print("Result is PROMOTED")
                else:
                    print("Result is FAIL")
             
                    
else:
    if m2 >=50: 
        if m3 >=50:
            if m4 >= 50:
                if m5 >= 50:
                    print("Result is PROMOTED")
    else:
        if m3 >= 50:
            print("Result is PROMOTED")
        else:
            if m4 >= 50:
                print("Result is PROMOTED")
            else:
                if m5 >= 50:
                    print("Result is PROMOTED")
                else:
                    print("Result is FAIL")
             
        


                    
    






