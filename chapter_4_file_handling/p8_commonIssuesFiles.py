with open('p1ccdjflkdjf.txt','rt') as f: # here if you write the wrong file name or the file doesn't exist it will raise a FileNotFoundError.
    content = f.read()
    print(content)

with open('p2.txt','rt') as f: 
    f.write("This is a test file created using the with statement.\n") # here if you try to write to a file that is opened in read mode it will raise an UnsupportedOperation error.
    f.close()
