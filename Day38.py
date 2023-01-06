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
    if len(word) >= 3:
        en_dec = None
        if type == 'encode':
            first_character = word[:1]
            rest_character = word[1:len(word)]
            en_dec = f"{random_string(length)}{rest_character}{first_character}{random_string(length)}"
        if type == 'decode':
            remove_first_three = word[3:len(word)]
            remove_last_three = remove_first_three[:len(remove_first_three)-3]
            get_last_one = remove_last_three[-1:]
            main_str = remove_first_three[:len(remove_last_three)-1]
            en_dec = f"{get_last_one}{main_str}"
        return en_dec
    else:
        return word[::-1]

output = simple_encode_decode(word='python', type='encode')


print(output)

# Encoded : veyythonpiaf
# Decoded : python

# Encoded : mfuavascriptjtyh
# Decoded : javascript
