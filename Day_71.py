"""
Multiple Inheritance in Python
------------------------------
Multiple inheritance is a powerful feature in object-oriented programming that allows a class to inherit attributes and methods from multiple parent classes.
This can be useful in situations where a class needs to inherit functionality from multiple sources.

"""


class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species

    def make_sound(self):
        print("Sound made by the animal")


class Mammal:
    def __init__(self, name, fur_color):
        self.name = name
        self.fur_color = fur_color


class Dog(Animal, Mammal):
    def __init__(self, name, breed, fur_color):
        Animal.__init__(self, name, species="Dog")
        Mammal.__init__(self, name, fur_color)
        self.breed = breed

    def make_sound(self):
        print("Bark!")