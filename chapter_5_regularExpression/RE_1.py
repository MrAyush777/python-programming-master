import re

message = "The current version of python is 3.10.5 and the latest version is 3.11.2, 11, 23, 34, 13, 24"

# print("python" in message) # returns True
# print('11' in message)
# print('12' in message)

# To find the index of a substring, use find methhod :

# print(message.find("python")) # returns 23

# search() method of re moudle :
# syntax : re.search(pattern, string/string object, [flags=0])

a = re.search("11",message)

print(a) # returns <re.Match object; span=(57, 59), match='11'>
print(message[68:70]) # returns 11

# we can use group() method to get the matched string from the match object.
# print(a.group()) #/'
# returns 11

# we can also write like this :
if(a):
    print("Found the pattern")
else:
    print("Pattern not found")

