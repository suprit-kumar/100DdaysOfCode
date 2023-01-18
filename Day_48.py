"""
Lambda Functions in Python
--------------------------
In Python, a lambda function is a small anonymous function without a name. It is defined using the lambda keyword

lambda arguments: expression

Lambda functions are often used in situations where a small function is required for a short period of time.
They are commonly used as arguments to higher-order functions, such as map, filter, and reduce.


# Function to double the input
def double(x):
  return x * 2

# Lambda function to double the input
lambda x: x * 2


Lambda functions can have multiple arguments, just like regular functions.
Here is an example of a lambda function with multiple arguments



# Function to calculate the product of two numbers
def multiply(x, y):
    return x * y

# Lambda function to calculate the product of two numbers
lambda x, y: x * y



Lambda functions can also include multiple statements, but they are limited to a single expression


# Lambda function to calculate the product of two numbers,
# with additional print statement
lambda x, y: print(f'{x} * {y} = {x * y}')


Lambda functions are often used in conjunction with higher-order functions, such as map, filter, and reduce
"""


# def double(x):
#   return x*2

def appl(fx, value):
  return 6 + fx(value)

double = lambda x: x * 2
cube = lambda x: x * x * x
avg = lambda x, y, z: (x + y + z) / 3

print(double(5))
print(cube(5))
print(avg(3, 5, 10))
print(appl(lambda x: x * x , 2))
