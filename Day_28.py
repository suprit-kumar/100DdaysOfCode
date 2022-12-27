# Docstrings in python

# Python docstrings are the string literals that appear right after
# the definition of a function, method, class, or module.

def square(n):
    '''Takes in a number n, returns the square of n'''
    print(n**2)
square(5)
print(square.__doc__)

# Python Comments vs Docstrings

# Python Comments
# Comments are descriptions that help programmers better understand the intent and functionality of the program.
# They are completely ignored by the Python interpreter.

# Python docstrings
# As mentioned above, Python docstrings are strings used right after the definition of a function, method, class, or module (like in Example 1).
# They are used to document our code.
#
# We can access these docstrings using the doc attribute.



# Python doc attribute
# Whenever string literals are present just after the definition of a function, module, class or method, they are associated with the object as their doc attribute.
# We can later use this attribute to retrieve this docstring.