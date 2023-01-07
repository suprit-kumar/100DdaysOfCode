'''
Write a python programme to translate a message into a secret code language. Use the rules below to
translate the normal English into a secret code language


Coding:
    if the word contains at least three characters. Remove the first characters and append it at the end
        now append three random characters at the starting and at the end
    else:
        simply reverse the string


Decoding:
    if the word contains less than three characters, reverse it
    else:
        remove random three characters from the start and from the end. Now remove the last letter and
        append at the beginning.
'''

import string
import random

def random_string(n):
    return ''.join(random.choices(string.ascii_lowercase, k=n))

def simple_encode_decode(word='', type=None):
    # type = encode/decode
    # For decoding the word provide the encoded word by this method
    length = 3
    if len(word) < 3:
        return word[::-1]

    first_character = word[:1]
    rest_character = word[1:]
    if type == 'encode':
        return f"{random_string(length)}{rest_character}{first_character}{random_string(length)}"
    if type == 'decode':
        main_str = word[3:-3]
        get_last_one = main_str[-1:]
        rest_str = main_str[:-1]
        return f"{get_last_one}{rest_str}"

output = simple_encode_decode(word='mfuavascriptjtyh', type='decode')


print(output)

# Example:

# Encoded : veyythonpiaf
# Decoded : python

# Encoded : mfuavascriptjtyh
# Decoded : javascript
