import re

# sub() function : is used to substitute a pattern with another string or substring. 
s1 = "Sunday Monday Tuesday Wednesday Thursday Friday Saturday Sunday Monday"
pat1 = "Sunday"
pat2 = r"S[a-z]+"

print(s1)
replacement = "Friday"

result = re.sub(pat1,replacement,s1) # it will replace the old substring by new substring
print(result)

result = re.sub(pat1,replacement,s1,count=1) # it will only replace the firs matched substring by new substring
print(result)

# ===========================================================================================

message = "We are learning re. Unsing RE, we can search for a pattern in a given string. Using sub(), we can replace the pattern with a given string as well."

pat3 = r"\bre\b"
replacement = r"regular expression"

result = re.sub(pat3,replacement,message)
print(result)

result = re.sub(pat3,replacement,message, flags=re.IGNORECASE) # it will replace re with regular expression even if the it is in upper case.
print(result)

phoneNumbers = "+91-8899334455, +91-9090901212"
pat4 = r"[+-]"
replacement = ""
result = re.sub(pat4,replacement,phoneNumbers)
print(result)
