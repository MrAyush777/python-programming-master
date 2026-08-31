# we will going to learn about the metacharacters in regular expressions. Metacharacters are characters that have a special meaning in regular expressions. They are used to define patterns and match specific types of characters or sequences in strings.

import re

message = "the current python version is 3.1. Other previous versions are 3.11, 3.55, 3.12."
a = "My house number is 803/C4"
# metacharecrer 1) = [] -> it returns a match if any of the characters inside the square brackets are found in the string. It is used to match a single character from a set of characters.

print(re.search("[0-9][0-9]",message))
# the search() methos only returns first match of the pattern from the string. If we want to find all the matches of the pattern in the string, we can use findall() method of re module.

print(re.search("[0-9][0-9][0-9]",a))

# ================================================================================================================

# metacharecrer 2) = . -> it returns a match if any character is found in the string. It is used to match any single character except newline character(\n).

print(re.search("[0-9].[0-9][0-9]",message))
print(re.search("[0-9].[0-9]",message))

print(re.search("[0-9].[0-9]",a))

# ================================================================================================================

# ^ - Caret -> it returns a match if the string starts with the character(S) specified after the caret(^). It is used to match the start of a string.
# it will check only from the starting not anywhere in the string. If not found it will return None otheriwise it will return a matchd object.

s1 = "python is a programing language"
pattern1 = r"^[a-z]{6}"
obj1 = re.search(pattern1,s1)
print(obj1)

# $ -> it returns a match if the string ends with the character(s) specified before the dollar sign($). It is used to match the end of a string.
pattern2 = r"[a-z]{8}$"
obj2 = re.search(pattern2,s1)
print(obj2)

# grouping -> it is used to group multiple characters together. It is used to match a specific sequence of characters in a string. It is denoted by parentheses ().
# 1) () + | (or) 
emails = "abc_123@example.edu random words and characters. x1y2z3.abc.edu"
pattern3 = r"(com|edu)" # matches either "com" or "edu"
obj3 = re.search(pattern3, emails)
print(obj3)

# 2) [] 
# it matches any single character from the set of characters specified inside the square brockets. It is used to match a single character from a set of characters.

