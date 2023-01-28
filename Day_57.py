"""
Access Specifiers/Modifiers
---------------------------
Access specifiers or access modifiers in python programming are used to limit the access of class variables and
class methods outside of class while implementing the concepts of inheritance.

Types of access specifiers
__________________________
1.Public access modifier
2.Private access modifier
3.Protected access modifier

Public Access Specifier in Python
---------------------------------
All the variables and methods (member functions) in python are by default public.
Any instance variable in a class followed by the ‘self’ keyword i.e. self.var_name are public accessed.

"""


class Student:
    # constructor is defined
    def __init__(self, age, name):
        self.age = age               # public variable
        self.name = name             # public variable

# obj = Student(21,"Harry")
# print(obj.age)
# print(obj.name)



class Student1:
    def __init__(self):
        self._name = "Harry"

    def _funName(self):      # protected method
        return "CodeWithHarry"

class Subject(Student1):       #inherited class
    pass

obj = Student1()
obj1 = Subject()
print(dir(obj))

# calling by object of Student class
print(obj._name)
print(obj._funName())
# calling by object of Subject class
print(obj1._name)
print(obj1._funName())