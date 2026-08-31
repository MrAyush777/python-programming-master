fh = open("p1.txt",'at') # is the file doesn't exist it will create a new file.
fh.write("\nThis line has been appended to the file.\n")
fh.write("append mode is used to add content to the existing file without overwriting the existing content.\n")
fh.close()