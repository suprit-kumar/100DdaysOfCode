"""
The time Module in Python
-------------------------
The time module in Python provides a set of functions to work with time-related operations, such as timekeeping,
formatting, and time conversions. This module is part of the Python Standard Library and
is available in all Python installations, making it a convenient and essential tool for a wide range of applications.

"""
import time

# def usingWhile():
#   i = 0
#   while i<50000:
#     i = i +1
#     print(i)

# def usingFor():
#   for i in range(50000):
#     print(i)

# init = time.time()
# usingFor()
# t1 = time.time() - init
# init = time.time()
# usingWhile()
# print(time.time() - init)
# print(t1)


# print(4)
# time.sleep(3)
# print("This is printed after 3 seconds")

t = time.localtime()
formatted_time = time.strftime("%Y-%m-%d %H:%M:%S", t)

print(formatted_time)