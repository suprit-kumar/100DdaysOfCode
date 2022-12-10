# Create a calculator capable of performing addition,subtraction,multiplication and division of two
# operators.


# -> The conversion of one type of data type into another type  of data type is knows as TypeCasting in python


def calculate_two_numbers():
    try:
        int_x = int(input("Enter First Number. Then press enter\n")) # Type casting numbers
        int_y = int(input("Enter Second Number. Then press enter\n"))

        print(f"Addition of two numbers: {int_x} + {int_y} = {int_x+int_y}\n"
              f"Subtraction of two numbers: {int_x} - {int_y} =  {int_x-int_y}\n"
              f"Multiplication of two numbers: {int_x} * {int_y} = {int_x*int_y}\n"
              f"Division of two numbers: {int_x} / {int_y} = {int_x/int_y}"
              )

    except:
        print('Entered value is not number. Please Enter Numbers.')


calculate_two_numbers()



# Implicit TypeCasting

c = 1.9 # float
d = 8 # int

ans = 9.9
# Python interpreter converted the result into higher data type
# where c remains same and d got converted into float
