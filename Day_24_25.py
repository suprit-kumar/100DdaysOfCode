# Python Tuples

# Tuples are ordered collection of data items.
# They store multiple items in a single variable.
# Tuple items are separated by commas and enclosed within round brackets ().
# Tuples are unchangeable meaning we can not alter them after creation.


tup = (1, 2, 76, 342, 32, "green", True)
# tup[0] = 90
print(type(tup), tup)
print(len(tup))
print(tup[0])
print(tup[-1])
print(tup[2])
# print(tup[34])

if  342 in tup:
  print("Yes 342 is present in this tuple")
tup2 = tup[1:4]
print(tup2)


# Operations on Tuple

# Manipulating Tuples

# Tuples are immutable, hence if you want to add, remove or change tuple items, then first you must convert the tuple to a list.
# Then perform operation on that list and convert it back to tuple.

countries = ("Spain", "Italy", "India", "England", "Germany")
temp = list(countries)
temp.append("Russia")       #add item
temp.pop(3)                 #remove item
temp[2] = "Finland"         #change item
countries = tuple(temp)
print(countries)