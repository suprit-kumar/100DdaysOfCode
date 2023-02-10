"""
Operator Overloading in Python: An Introduction
-----------------------------------------------
Operator Overloading is a feature in Python that allows developers to redefine the behavior of mathematical and comparison operators for custom data types.
This means that you can use the standard mathematical operators (+, -, *, /, etc.) and comparison operators (>, <, ==, etc.) in your own classes,
just as you would for built-in data types like int, float, and str.


For example, if you want to overload the + operator to add two instances of a custom class,
you would define the add method:


"""

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"{self.x}x + {self.y}y"

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)


v1 = Point(3, 5)
print(v1)