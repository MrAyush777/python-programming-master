import re

# match() function : it is used to match a pattern at the beginning of a string. It returns a match object if the pattern is found at the beginning of the string, otherwise it returns None. 

s1 = "We are learning regex in python"
pattern1 = r"[A-Z][a-z]"
matchObj1= re.match(pattern1,s1)
print(matchObj1)

pattern2 = r"[a-z]{3}"
matchObj2 = re.match(pattern2,s1)
print(matchObj2) # returns None, because the pettern is not found at the beginning.

# =================================================================================================================

phones = "John-8448483999, Peter-8429094849, Sam-8484844848"
pattern3 = r"[0-9]{10}"
matchObj3 = re.search(pattern3,phones)
print(matchObj3)

# findall() function : it is used to find all the occurrences of a pattern in a string. It returns a list of all the matches found in the string. If no matches are found, it returns None.

phones = "John-8448483999, Peter-8429094849, Sam-8484844848, Tony-8484487, Don-848448844884484899,Python 3.13.12"
pattern3 = r"[0-9]{10}" # it will returns all numbers that have length of 10 exactly. 
matchObj3 = re.findall(pattern3,phones)
print(matchObj3)

pattern3 = r"[0-9]+" # it will return all the numbers from the string.
matchObj3 = re.findall(pattern3,phones)
print(matchObj3)

# fetch all phone numbers. The phone number are exactly 7 digits and should not exceed 15 digits.
pattern3 = r"[0-9]{7,15}" # it will return all the numbers from the string.
# instead we also can write like this : r"[0-9]{7,} -> it means 7 or more digits allowed
matchObj3 = re.findall(pattern3,phones)
print(matchObj3)

# fetch all phone numbers. The phone number are atleast 7 digits
pattern3 = r"[0-9]{7,}" # r"[0-9]{7,} -> it means 7 or more digits allowed
matchObj3 = re.findall(pattern3,phones)
print(matchObj3)

# \b - it's called boundary 
pattern3 = r"[0-9]{7,15}\b" # it will return all the numbers from the string.
matchObj3 = re.findall(pattern3,phones)
print(matchObj3)


# finditer() function : it give us individual outputs for each matching object from the string instead of List.

pattern4 = r"\b[0-9]{7,15}\b"
matchObj4 = re.finditer(pattern4,phones)
print(matchObj4) # it will return callable_iterator object at 0x000001B83FSF1F30

# To get the actual output use for loop like below :

for matches in matchObj4:
    print(matches) # it will return each all mathchig objects individualy in the format of : <re.Match object; span=(5, 15), match='8448483999'> 





      





