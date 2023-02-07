"""
Super keyword in Python
-----------------------
The super() keyword in Python is used to refer to the parent class.
It is especially useful when a class inherits from multiple parent classes and
you want to call a method from one of the parent classes.


When a class inherits from a parent class, it can override or extend the methods defined in the parent class.
However, sometimes you might want to use the parent class method in the child class.
This is where the super() keyword comes in handy.


"""
class ParentClass:
    def parent_method(self):
        print("This is the parent method.")

class ChildClass(ParentClass):
    def child_method(self):
        print("This is the child method.")
        super().parent_method()

child_object = ChildClass()
child_object.child_method()






