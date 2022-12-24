# Loops - For , While

# or loops can iterate over a sequence of iterable objects in python.
# Iterating over a sequence is nothing but iterating over strings, lists, tuples, sets and dictionaries.

# Exampel - 1
# colors = ["Red", "Green", "Blue", "Yellow"]
# for color in colors:
#   print(color)
#   for i in color:
#     print(i)
#
# # Exampel - 2
# for k in range(1, 12, 3):
#   print(k)


# While Loop
# As the name suggests, while loops execute statements while the condition is True.
# As soon as the condition becomes False, the interpreter comes out of the while loop.


i = 0

while i <= 10:
    print("I value: ",i)
    i = i+1

# Break and continue
# The break statement enables a program to skip over a part of the code.
# A break statement terminates the very loop it lies within.

for i in range(5):
    if i == 3:
        break
    print(i)