# String Methods
# Few examples
# String are immutable. But you can change the strings and that changed string will another copy

a = "!!!Garry!!!!!!!!!!!!!"
b = "Albert Einstein"
print(len(a))
print(a.upper()) # As we know strings are immutable. So this method operates in existing string and returns a new string
print(a.lower())
print(a.rstrip("!")) # Remove Only trailing strips

print(a.replace("Garry","John"))

print(b.split(" ")) # returns list

blogHeading = "introduction to js"

print(blogHeading.capitalize())

str1 = "Welcome to the console!!!"

print(str1.center(50)) # Aligns to the center as per the parameter given by the user.

print(a.count("!")) # Counts the number of occurances

print(str1.endswith("!!!")) # Returns boolean

print(str1.endswith("to",4,10)) # Check for value in-between the string by providing start and end index position

str2 = "Her name is Danny, She is an innocent women."

print(str2.find("is")) # Returns the first occurance index of given value. If value is absent from the string returns -1.

print(str2.index('is')) # Returns the index of the given value. If value absent throws error.

str3 = "RamAgeis12"

print(str3.isalnum()) # Check string alphanumeric A-Z,a-z,0-9
print(str3.isalpha()) # A-Z,a-z

# Explore more. There is many more methods written in python

# isprintable
# istitile
# startswith
# and many more ..............