"""
Python Class and Objects
------------------------
A class is a blueprint or a template for creating objects,
providing initial values for state (member variables or attributes),
and implementations of behavior (member functions or methods).
The user-defined objects are created using the class keyword

Object is the instance of the class used to access the properties of the class Now lets create an object of the class
"""


class Person:
  name = "Harry"
  occupation = "Software Developer"
  networth = 10
  def info(self):
    print(f"{self.name} is a {self.occupation}")


a = Person()
b = Person()
c = Person()

a.name = "Shubham"
a.occupation = "Accountant"

b.name = "Nitika"
b.occupation = "HR"

# print(a.name, a.occupation)
a.info()
b.info()
c.info()
