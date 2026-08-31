# compile() function - 
import re

phones = "Alice-9744834924, Mark-7748228523, Carol-8484484444" 
pattern1 = r"\d{10}"
matchObj = re.findall(pattern1,phones)
print(matchObj)
