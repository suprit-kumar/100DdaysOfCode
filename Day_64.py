"""
Class Methods as Alternative Constructors
-----------------------------------------
In object-oriented programming, the term "constructor" refers to a special type of method that is automatically executed when an object is created from a class.
The purpose of a constructor is to initialize the object's attributes, allowing the object to be fully functional and ready to use.


However, there are times when you may want to create an object in a different way, or with different initial values,
than what is provided by the default constructor.
This is where class methods can be used as alternative constructors.


A class method belongs to the class rather than to an instance of the class. One common use case for class methods as alternative
constructors is when you want to create an object from data that is stored in a different format, such as a string or a dictionary.
For example, consider a class named "Person" that has two attributes: "name" and "age".



But what if you want to create a Person object from a string that contains
the person's name and age, separated by a comma? You can define a class method named "from_string" to do this
"""


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @classmethod
    def from_string(cls, string):
        name, age = string.split(',')
        return cls(name, int(age))

person = Person.from_string("John Doe, 30")
print(person.name)
print(person.age)