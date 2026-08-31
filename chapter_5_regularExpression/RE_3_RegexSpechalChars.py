import re

s1 = "Python is a programming language. I am python3.14"

pattern1 = "old\new" 
pattern2 = r"old\new" 

# here we put 'r' in front of pattern for raw string. If we use anything, a special character will not take its special meaning. It will be treated as a normal character. For example, if we use '\n' in pattern, it will be treated as a new line character. But if we use 'r\n' in pattern, it will be treated as a normal character.
print(pattern1) # if we not write 'r' in front of pattern, it will print a new line character. But if we write 'r' in front of pattern, it will print '\n' as a normal character.
print(pattern2) # output : old\new


pattern3 = r"[A-Z][a-z][a-z]"
matchObj = re.search(pattern3,s1)
print(matchObj)

# ==============================================================================================

# special characters in regex : \d, \D, \s, \S, \w, \W

# ==============================================================================================

# 1) \d and \D : \d is used to match any digit from 0 to 9. It is equivalent to [0-9]. \D is used to match any non-digit character. It is equivalent to [^0-9].

# \d -> matches any digit from 0 to 9.
pattern4 = r"[a-z][a-z][a-z]\d" 
ans1 = re.search(pattern4,s1)
print(ans1)

# \D -> mathches any non-digit character.
pattern5 = r"[a-z][a-z][a-z]\D"
ans2 = re.search(pattern5,s1)
print(ans2)

# 2) \s and \S : \s is used to match any whitespace character. It is equivalent to [ \t\n\r\f\v]. \S is used to match any non-whitespace character. It is equivalent to [^ \t\n\r\f\v].

# \s : matches any whitespace charater.

pattern6 = r"[a-z][a-z][a-z]\s"
ans3 = re.search(pattern6,s1)
print(ans3)


s2 = """Hi there$
We are learning python
"""

print(s2)
pattern7 = r"[a-z][a-z][a-z]\s"
ans4 = re.search(pattern7,s2)
print(ans4)


# \S - it is opposite of \s. It matches any non-whitespace character like \n, \t, \r, \f, \v, space etc.

print(s2)
pattern7 = r"[a-z][a-z][a-z]\S"
ans4 = re.search(pattern7,s2)
print(ans4)


# 3 \w and \W : \w is used to match any alphanumeric character. It is equivalent to [a-zA-Z0-9_]. \W is used to match any non-alphanumeric character. It is equivalent to [^a-zA-Z0-9_].

# \w -> matches any alphanumeric character. It is equivalent to [a-zA-Z0-9_]. / [a-z], [A-Z], [0-9], _
pattern8 = r"[a-z][a-z][a-z]\w"
ans5 = re.search(pattern8,s2)
print(ans5)

# \W -> opposite of \w, matches a character except alphanumeric character. ([a-zA-Z0-9_])
pattern9 = r"[a-z][a-z][a-z]\W"
ans6 = re.search(pattern9,s2)
print(ans6)