# x mode = create a file
fh = open("p2.txt","x")

# writing into a file
fh.write("this is a new file created using x mode")
fh.write("\nthis is the second line of the file...")

fh.close()
# fh.write("fuck you jani") # this will raise an error because the file is closed
# if the file is already exist, we can't create it again...