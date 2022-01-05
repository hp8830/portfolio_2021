"""The pair of functions chr() and ord() can be used to create a character using its codepoint, and to determine a codepoint corresponding to a character. Both of the following expressions are always true:

5. Some other functions that can be applied to strings are:

list() – create a list consisting of all the string's characters;
max() – finds the character with the maximal codepoint;
min() – finds the character with the minimal codepoint.

"""
character = "d"
codepoint = "f"
chr(ord(character)) == character
ord(chr(codepoint)) == codepoint

