"""
Constructors
-----------
A constructor is a special method in a class used to create and initialize an object of a class.
There are different types of constructors.
Constructor is invoked automatically when an object of a class is created.


A constructor is a unique function that gets called automatically when an object is created of a class.
The main purpose of a constructor is to initialize or assign values to the data members of that class.
It cannot return any value other than None.


init is one of the reserved functions in Python. In Object Oriented Programming, it is known as a constructor.


Types of Constructors in Python
------------------------------
1.Parameterized Constructor
2.Default Constructor


Parameterized Constructor in Python
-----------------------------------
When the constructor accepts arguments along with self, it is known as parameterized constructor.

Default Constructor in Python
----------------------------
When the constructor doesn't accept any arguments from the object and has only one argument,
self, in the constructor, it is known as a Default constructor.



"""


class Person:

  def __init__(self, name, occ):
    print("Hey I am a person")
    self.name = name
    self.occ = occ

  def info(self):
    print(f"{self.name} is a {self.occ}")


a = Person("Harry", "Developer")
b = Person("Divya", "HR")
a.info()
b.info()
# print(a.name)
# a.name = "Divya"
# a.occ = "HR"
# a.info()
