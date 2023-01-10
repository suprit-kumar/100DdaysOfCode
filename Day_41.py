"""
How importing in python works
-----------------------------
Importing in Python is the process of loading code from a Python module into the current script.
This allows you to use the functions and variables defined in the module in your current script,
as well as any additional modules that the imported module may depend on.


from keyword
-------------
You can also import specific functions or variables from a module using the "from" keyword.
For example, to import only the sqrt function from the math module, you would write:

from math import sqrt, pi

result = sqrt(9)
print(result)  # Output: 3.0

print(pi)  # Output: 3.141592653589793


importing everything
--------------------
from math import *

result = sqrt(9)
print(result)  # Output: 3.0

print(pi)  # Output: 3.141592653589793



The dir function
----------------
Finally, Python has a built-in function called dir that you can use to view the names of all the functions and variables defined in a module.
This can be helpful for exploring and understanding the contents of a new module.

import math

print(dir(math))


This will output a list of all the names defined in the math module,
including functions like sqrt and pi, as well as other variables and constants.

In summary, the import statement in Python allows you to access the functions and variables defined in a module from within your current script.
You can import the entire module, specific functions or variables, or use the * wildcard to import everything.
You can also use the as keyword to rename a module, and the dir function to view the contents of a module.



"""