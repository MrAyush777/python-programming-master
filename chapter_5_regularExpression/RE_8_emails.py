import re
with open("students_details","rt") as fh:
    data = fh.read()

pattern = r"\b[a-zA-Z]+[\w.-]+[@][a-z]+[.][a-z]+\b"
matchObj = re.finditer(pattern,data)

for matches in matchObj:
    print(matches)
