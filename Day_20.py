# Functions

# A function is a block of code that performs a specific task whenever it is called. In bigger programs, where we have large amounts of code,
# it is advisable to create or use existing functions that make the program flow organized and neat.


# There are two types of functions:
#
# Built-in functions
# User-defined functions

# Built-in functions:
# These functions are defined and pre-coded in python. Some examples of built-in functions are as follows:
#
# min(), max(), len(), sum(), type(), range(), dict(), list(), tuple(), set(), print(), etc.
#
# User-defined functions:
# We can create functions to perform specific tasks as per our needs. Such functions are called user-defined functions.


def isGreater(a, b):
  if(a>b):
    print("First number is greater")
  else:
    print("Second number is greater or equal")

isGreater(5,6)