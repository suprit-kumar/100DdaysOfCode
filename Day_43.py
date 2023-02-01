"""
os Module in Python
-------------------
The os module in Python is a built-in library that provides functions for interacting with the operating system.
It allows you to perform a wide variety of tasks, such as reading and writing files,
interacting with the file system, and running system commands.

"""


import os
if(not os.path.exists("data")):
    os.mknod(f"{os.getcwd()}/Day_{60}.py")



"""
Interacting with the file system
--------------------------------
The os module also provides functions for interacting with the file system. 
For example, you can use the os.listdir function to get a list of the files in a directory:
"""


# Get a list of the files in the current directory
files = os.listdir(".")
# print(files)

