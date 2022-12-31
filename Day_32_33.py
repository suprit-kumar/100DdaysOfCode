# Python Dictionaries

# Dictionaries are ordered collection of data items.
# They store multiple items in a single variable.
# Dictionary items are key-value pairs that are separated by commas and enclosed within curly brackets {}.


info = {'name': 'Karan', 'age': 19, 'eligible': True}
print(info)
print('---------------------------------------------')
print(info.keys())
print('---------------------------------------------')
print(info.values())
print('---------------------------------------------')
for key in info.keys():
  print(f"The value corresponding to the key {key} is {info[key]}")

print('---------------------------------------------')
print(info.items())
print('---------------------------------------------')
for key, value in info.items():
    print(f"The value corresponding to the key {key} is {value}")

print('----------------------Dictionary Methods----------------------')
# Dictionary Methods

# update():

# The update() method updates the value of the key provided to it if the item already exists in the dictionary,
# else it creates a new key-value pair.

# clear():
# The clear() method removes all the items from the list.

# pop():
# The pop() method removes the key-value pair whose key is passed as a parameter.

# popitem():
# The popitem() method removes the last key-value pair from the dictionary.


# del:
# we can also use the del keyword to remove a dictionary item.


# If key is not provided, then the del keyword will delete the dictionary entirely.

ep1 = {122: 45, 123: 89, 567: 69, 670: 69}
ep2 = {222: 67, 566: 90}

# ep1.update(ep2)
# ep1.clear()
# ep1.pop(122)
# ep1.popitem()
del ep1[122]
print(ep1)