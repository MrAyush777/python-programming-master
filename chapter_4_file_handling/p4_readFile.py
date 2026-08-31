fileHandler = open("p1.txt",'rt')

# read operation
# content1 = fileHandler.read() # reads the contents of the file as string.
# print(content1)
# print(type(content1)) # str 

# content2 = fileHandler.read(10) # reads the next 10 characters from the file
# print(content2)
# print(type(content2)) # str 

# readline() :
'''
line1 = fileHandler.readline()
line2 = fileHandler.readline()
line3 = fileHandler.readline() 
line4 = fileHandler.readline() # empty string => the file has reached the End of File (EOF)
print(f"line 1 : {line1}")
print(f"line 2 : {line2}")
print(f"line 3 : {line3}")
print(f"line 4 : {line4}") # it will return empty string if ther is no more line to read.
'''

# readlines() : it reads all the lines of the file and returns a list of lines.
lines = fileHandler.readlines()
print(lines)
print(type(lines)) # list
for line in lines:
    print(line.strip()) # strip() is used to remove the newline character from the end of the line.
    # you can use rstrip() to remove the newline character from the end of the line.     

fileHandler.close() 