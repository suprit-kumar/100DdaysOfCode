"""
Hybrid Inheritance in Python
----------------------------
Hybrid inheritance is a combination of multiple inheritance and single inheritance in object-oriented programming.
It is a type of inheritance in which multiple inheritance is used to inherit the properties of multiple base classes
into a single derived class, and single inheritance is used to inherit the properties of the derived class into a sub-derived class.


In Python, hybrid inheritance can be implemented by creating a class hierarchy,
in which a base class is inherited by multiple derived classes,
and one of the derived classes is further inherited by a sub-derived class.



class BaseClass1:
  # attributes and methods

class BaseClass2:
  # attributes and methods

class DerivedClass(BaseClass1, BaseClass2):
  # attributes and methods



Example
-------
Consider the example of a Student class that inherits from the Person class,
which in turn inherits from the Human class.
The Student class also has a Program class that it is associated with.


"""


class Human:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show_details(self):
        print("Name:", self.name)
        print("Age:", self.age)


class Person(Human):
    def __init__(self, name, age, address):
        Human.__init__(self, name, age)
        self.address = address

    def show_details(self):
        Human.show_details(self)
        print("Address:", self.address)


class Program:
    def __init__(self, program_name, duration):
        self.program_name = program_name
        self.duration = duration

    def show_details(self):
        print("Program Name:", self.program_name)
        print("Duration:", self.duration)


class Student(Person):
    def __init__(self, name, age, address, program):
        Person.__init__(self, name, age, address)
        self.program = program

    def show_details(self):
        Person.show_details(self)
        self.program.show_details()



program = Program("Computer Science", 4)
student = Student("John Doe", 25, "123 Main St.", program)
student.show_details()
