# compile time errors = syntax error & indentention error
# exception = run time errors / errors during execution
# we can have multiple except blocks with try block. There can be only one try block.

import io


# try:
#     a = int(input("Enter the value : "))
#     b = int(input("Enter the value : "))
#     r = a/b
#     print(r)
# except ZeroDivisionError:
#     print("the denomiter cannot be 0 ")
# except ValueError:
#     print("Input should only be digits not any other characters...")


# =======================================================================================


# try:
    
#     with open("p2.txt",'rt') as fs:
#         data = fs.readline()
#         print(data)
# except FileNotFoundError as fnf: # here we store the error in the variable called 'fnf'
#     print("file not found please write correct file  name here..")
#     print(fnf) # it will print the error in text format in the terminal.
# else: # this block will executed only when try block not consist any errors/exceptions
#     print("Programe not have any exceptions...")
    
    
# =======================================================================================



try:
    
    fh = open("p9.txt",'wt')
    data = fh.read()
    fh.close()
except io.UnsupportedOperation as io_err:
    print("Error :",io_err)
else:
    print("Something get wrong !")
finally:
    print("I am done now. Have a nice day")
