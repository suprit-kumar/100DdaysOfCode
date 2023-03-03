"""
Regular Expressions in Python
-----------------------------
Regular expressions, or "regex" for short, are a powerful tool for working with strings and text data in Python.
They allow you to match and manipulate strings based on patterns,
making it easy to perform complex string operations with just a few lines of code.



Metacharacters in regular expressions
-------------------------------------
[]  Represent a character class
^   Matches the beginning
$   Matches the end
.   Matches any character except newline
?   Matches zero or one occurrence.
|   Means OR (Matches with any of the characters
    separated by it.
*   Any number of occurrences (including 0 occurrences)
+   One or more occurrences
{}  Indicate number of occurrences of a preceding RE
    to match.
()  Enclose a group of REs
"""


import re
# Searching for a pattern in re using re.search() Method

pattern = r"[A-Z]+yclodne"
text = '''Cyclone Dumazile was a strong tropical cyclone in the South-West Indian Ocean that affected Madagascar and Réunion in early March 2018. Dumazile originated from a cyclone Dyclone low-pressure area that formed near Agaléga on 27 February. It became a tropical disturbance on 2 March, and was named the next day after attaining tropical storm status. Dumazile reached its peak intensity on 5 March, with 10-minute sustained winds of 165 km/h (105 mph), 1-minute sustained winds of 205 km/h (125 mph), and a central atmospheric pressure of 945 hPa (27.91 inHg). As it tracked southeastwards, Dumazile weakened steadily over the next couple of days due to wind shear, and became a post-tropical cyclone on 7 March

'''

match = re.search(pattern, text)
print(match)


matches = re.finditer(pattern, text)
for match in matches:
  print(match.span())
  print(text[match.span()[0]: match.span()[1]])