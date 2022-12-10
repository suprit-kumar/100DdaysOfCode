# In Python anything that you enclose between single or double quotes is considered as a string.
# String is essentially a sequence of array of textual data.
# Strings are used when working with unicode characters.


info = '''
In Python anything that you enclose between single or double quotes is considered as a string.
String is essentially a sequence of array of textual data.
Strings are used when working with unicode characters.
'''
# print(info)


word = "Python,Is,single"

# for char in word:
#     print(char)


# String Slicing

print(len(word))  # Length of the strings
print(word[:5])  # Start and Stop index, Stop is excluded .. Print 0->4 index
print(word[2:5])
print(word[0:-3])  # Negative slicing -> Slice last 3 strings
print(word[::-1])  # Reverse the string

