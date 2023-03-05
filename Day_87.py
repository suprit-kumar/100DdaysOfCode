"""
Multithreading in Python
------------------------
Multithreading is a technique in programming that allows multiple threads of execution to run concurrently within a single process.
In Python, we can use the threading module to implement multithreading.
In this tutorial, we will take a closer look at the threading module and its various functions and how they can be used in Python.

"""

import threading
import time
from concurrent.futures import ThreadPoolExecutor


# Indicates some task being done
def func(seconds):
    print(f"Sleeping for {seconds} seconds")
    time.sleep(seconds)
    return seconds


def main():
    time1 = time.perf_counter()
    # Normal Code
    # func(4)
    # func(2)
    # func(1)

    # Same code using Threads
    t1 = threading.Thread(target=func, args=[4])
    t2 = threading.Thread(target=func, args=[2])
    t3 = threading.Thread(target=func, args=[1])
    t1.start()
    t2.start()
    t3.start()

    # t1.join()
    # t2.join() # wait until t1 finished
    # t3.join() # wait until t2 finished
    # Calculating Time
    time2 = time.perf_counter()
    print(time2 - time1)


main()