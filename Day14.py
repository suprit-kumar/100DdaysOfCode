# if-else statements - When programme wants to verify certain condition or checks some data

# Some conditional operatros - >,<,>=,<=,==,!= etc..

age = int(input("Enter you age:  "))
print(f"Your age is: {age}")

if age>18 and age<=59:
    print("Congratulations!!! You can drive.")
elif age >= 60:
    print(f"You are now {age}. It is advisable to you that, You shouldn't drive at this age.")
else:
    print("Sorry!!! You can not derive.")