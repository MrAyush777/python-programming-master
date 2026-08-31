# to print the length of the string 'len()' function is used 

name = "ayush fataniya"

print(len(name)) 
# it returns the length of 'value' of variable

print(name.endswith("j")) # it returns boolean value , returns true if condition is true otherwise returns false, here the condition is a name is ends with 'j' but name is actually ends with 'h' so that the condiom returns false.

print(name.startswith("A")) # it returns boolean value , returns true if condition is true otherwise returns false, here the condition is a name is start with 'a' and name is actually start with 'a' so that the condiom returns true.

print(name.capitalize())
# it will capitalize the first alphabet of the string (only one starting alphabet)

print(name.count("y"))
# it will count that how many alphabet are there in the string that we enter in the 'count() function'

print(name.find("fata"))
# it returns the index of the string where the word was found.

replaceString = name.replace("Ayush","Mahi")
print(replaceString)
# it replace the old word with new word in the entire string.

""""""""""""""""""""""""""" Escape Seqauence Characters """""""""""""""""""""""""""""""""

ESC1 = "ayush is a good boy \nbut not the \t bad boy"
print(ESC1)
# here we use '\n' ESC(Escape Sequence Character) that adds new line in the existing string. 
# and than we use '\t' ESC that adds tab in the existing string.

ESC2 = "i am the good \"boy\" not you ?"
print(ESC2)
# if you want to use double quotes inside the string than you need to use ' \" ' to use double quotes inside the string.

ESC3 = "i want to use backslash \\ in this string"
print(ESC3)
# if you want to use backslash than use double backslash inside the string.