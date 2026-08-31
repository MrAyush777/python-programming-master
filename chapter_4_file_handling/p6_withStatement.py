# a 'with' statement in python is used to wrap the execution of a block of code within methods defined by a context manager. It is commonly used for resource management, such as opening and closing files, ensuring that resources are properly released after their use.
# the with statement in python simplifies resource management by automatically handling the setup and cleanup tasks. 

with open('p1.txt','rt') as f:
    content = f.read()
    print(content)
    
with open('p6_test.txt','xt') as x:
    x.write("this is a test file created using the with statement.\n")
    x.write("the with statement ensures that the file is properly closed after its suite finishes, even if an exception is raised at some point.\n")
