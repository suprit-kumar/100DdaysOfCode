# Recursion in python

# Recursion is the process of defining something in terms of itself.

# Python Recursive Function

# In Python, we know that a function can call other functions.
# It is even possible for the function to call itself.
# These types of construct are termed as recursive functions.

# Example
# factorial(7) = 7*6*5*4*3*2*1
# factorial(6) = 6*5*4*3*2*1
# factorial(5) = 5*4*3*2*1
# factorial(4) = 4*3*2*1
# factorial(0) = 1

# Normal Function

def find_factorial(n):
    factorial = 1
    while n >= 1:
        factorial = factorial * n
        n = n - 1
    return factorial


# print(find_factorial(1))


# Recursion
def find_factorial_recursively(n):
    if n in [0, 1]:
        return 1
    else:
        return n * find_factorial_recursively(n - 1)
        #


# print(find_factorial_recursively(7))
# 7 * find_factorial_recursively(6)
# 7 * 6 * find_factorial_recursively(5)
# 7 * 6 * 5 * find_factorial_recursively(4)
# 7 * 6 * 5 * 4 * find_factorial_recursively(3)
# 7 * 6 * 5 * 4 * 3 * find_factorial_recursively(2)
# 7 * 6 * 5 * 4 * 3 * 2 * find_factorial_recursively(1)
# 7 * 6 * 5 * 4 * 3 * 2 * 1


# Write a programmer to print Fibonacci sequence
# f(0)=0
# f(1)=1
# f(2)=f1+f2 #1
# f(3)=f2+f1 #2
# f(4)=f3+f2 #3


# f(n) = f(n-1) + f(n-2)


# Normal Function
def find_fibonacci(n):
    n_1 = 0
    n_2 = 1
    count = 0
    if n <= 0:
        print("Please enter a positive integer, the given number is not valid")
    elif n == 1:
        print(n_1)
    else:
        print("The fibonacci sequence of the numbers is:")
        while count <= n:
            print(n_1)
            nth = n_1 + n_2
            n_1 = n_2
            n_2 = nth
            count += 1


# find_fibonacci(13)


# Recursion
def fibonacci_recursive(n):
    if n < 0:
        print("Please enter a positive integer, the given number is not valid")
    elif n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci_recursive(n-1) + fibonacci_recursive(n-2)

print(fibonacci_recursive(6))