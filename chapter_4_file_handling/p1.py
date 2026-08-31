# mainly in pytyon files are classiffied into two types : 1) text file and 2) binary file

# opening a file in python
# open("fileName","modeToOpen")
# modes : r(read-(default mode)) , w(write) , a(append) , x(create) , t(text) , b(binary)

file = open("p1.txt","rt") # this will open the file in read an text mode.
# here you can write "rt" or "r" or "tr" all are same and will open the file in read and text mode.
# if you dont specify the mode then by default it will open the file in read and text mode.


print(file) # it will return file object with its location in mrmory and the mode in which it is opened.
# this object : _io.TextIOWrapper : is nothing bua a file object which is used to perform various operations on the file like reading, writing, etc.
# it is file itself.

# closing a file :
file.close()