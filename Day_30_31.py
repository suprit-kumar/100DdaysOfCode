# Python Sets

# Sets are unordered collection of data items.
# They store multiple items in a single variable.
# Set items are separated by commas and enclosed within curly brackets {}. Sets are unchangeable,
# meaning you cannot change items of the set once created. Sets do not contain duplicate items.

# s = {2, 4, 2, 6}
# print(s)
#
# info = {"Carla", 19, False, 5.9, 19}
# print(info)
#
# harry = set()
# print(type(harry))
#
# for value in info:
#   print(value)

print('--------------------------------------------------------')
# I. union() and update():

cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities2 = {"Tokyo", "Seoul", "Kabul", "Madrid"}
cities3 = cities.union(cities2) # Returns new set
print(cities3)

cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities2 = {"Tokyo", "Seoul", "Kabul", "Madrid"}
cities.update(cities2) # Update in existing set
print(cities)

print('--------------------------------------------------------')
# II. intersection and intersection_update():

# The intersection() and intersection_update() methods prints only items that are similar to both the sets.
# The intersection() method returns a new set whereas intersection_update() method updates into the existing set from another set.


cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities2 = {"Tokyo", "Seoul", "Kabul", "Madrid"}
cities3 = cities.intersection(cities2)
print(cities3)


cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities2 = {"Tokyo", "Seoul", "Kabul", "Madrid"}
cities.intersection_update(cities2)
print(cities)
print('--------------------------------------------------------')

# III. symmetric_difference and symmetric_difference_update():

# The symmetric_difference() and symmetric_difference_update() methods prints only items that are not similar to both the sets.
# The symmetric_difference() method returns a new set whereas symmetric_difference_update() method updates into the existing set from another set.

cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities2 = {"Tokyo", "Seoul", "Kabul", "Madrid"}
cities3 = cities.symmetric_difference(cities2)
print(cities3)

cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities2 = {"Tokyo", "Seoul", "Kabul", "Madrid"}
cities.symmetric_difference_update(cities2)
print(cities)
print('--------------------------------------------------------')
# IV. difference() and difference_update():

# The difference() and difference_update() methods prints only items that are only present in the original set and not in both the sets.
# The difference() method returns a new set whereas difference_update() method updates into the existing set from another set.

cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities2 = {"Seoul", "Kabul", "Delhi"}
cities3 = cities.difference(cities2)
print(cities3)

cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities2 = {"Seoul", "Kabul", "Delhi"}
print(cities.difference_update(cities2))