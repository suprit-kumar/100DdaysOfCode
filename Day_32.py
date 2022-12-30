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
