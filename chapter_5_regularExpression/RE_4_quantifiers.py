# Quantifiers : these are symbols or characters used for telling how much quantiry of particular special character you want to match in your string. Quantifiers are used to specify the number of occurrences of a character or group of characters in a regular expression pattern.

import re

message = "The current python version is 3.13. Other previous versions are 3.12, 3.11, 3.10, 3.9, 3.8, 3.7, 3.6, 3.5, 3.4, 3.3, 3.2, 3.1 and so on."

# pattern1 = r"[a-z][a-z][a-z][a-z]" this is long and not a good way to write pattern. Instead we can use quantifiers to specify how many times we want to match a particular character.    
# instead we can write like this : 

pattern2 = r"[a-z]{4}" # here we are using quantifier {4} to specify that we want to match 4 occurrences of [a-z] in our string. It is equivalent to [a-z][a-z][a-z][a-z].
pattern3 = r"[a-z]{6}" # it will try to search for exactly 6 occurrences of [a-z] in our string.
pattern4 = r"[a-z]{2,4}" # it will try to search for minimum 2 and maximum 4 occurrences of [a-z] in our string.

matchObj1 = re.search(pattern2, message)
print(matchObj1)

matchObj2 = re.search(pattern3, message)
print(matchObj2)

matchObj3 = re.search(pattern4, message)
print("obj 3 ",matchObj3)

# +  -> matches 1 or more repetitions of previous pattern. It is equivalent to {1,}. It will try to search for 1 or more occurrences of [a-z] in our string.
patt1 = r"[A-Z][a-z][a-z]+"
matchObj4 = re.search(patt1, message)
print(matchObj4)

# ?  -> matches 0 or 1 repetitions of previous pattern. It is equivalent to {0,1}. It will try to search for 0 or 1 occurrences of [a-z] in our string.
patt2 = r"[A-Z][a-z][a-z]?"
matchObj5 = re.search(patt2, message)
print(matchObj5)    

# * -> 0 or more repetitions of the previous pattern. 
patt3 = r"[A-Z][a-z][a-z]*"
matchObj6 = re.search(patt3, message)
print("obj 6",matchObj6)

