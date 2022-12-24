# Match case statements
# Works only above python 3.10 and above
# To implement switch-case like characteristics very similar to if-else functionality, we use a match case in python.
# A match statement will compare a given variable’s value to different shapes, also referred to as the pattern. The main idea is to keep on comparing the variable with all the present patterns until it fits into one.


x = int(input("Enter the value of x: "))
# x is the variable to match
match x:
    # if x is 0
    case 0:
        print("x is zero")
    # case with if-condition
    case 4:
        print("case is 4")
    case _ if x != 90:
        print(x, "is not 90")
    case _:  # _ is default match
        print(x, "is not 80")
