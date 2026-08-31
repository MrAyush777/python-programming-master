# The functions that are defined inside a class is known as Methods. or we can say that any function that get's defined insed a class becomes automatically method of that class. 
# so that append method does not append the function.

# class MyClass:
    # pass # pass is a keyword that is used to make code syntactically correct. We can use this whenever we want to make an empty class.


# creating an object. Below obj1 and obj2 are objects of MyClass.    
# obj1 = MyClass()
# obj2 = MyClass()
# l1 = [10,20,30]

# print(type(l1)) # output : <class 'list'> 
# print(type(obj1)) # output : <class '__main__.MyClass'>
# print(type(obj2)) # output : <class '__main__.MyClass'>

# here anything starting and ending with double underscore is called 'Dunder'. D means Double and Under means Underscore. This is special method or have special meaning in python.

# Calling methods using objects : using '.' notations 
# syntax : object.method(arguments)

# =========================================================================================================================

class Student:
    """
    This a class Student to manage activities and informations of the students.
    """
    pass

s1 = Student()
s2 = Student()

# Doc string :  it is nothing but the documentation about the class. use '__doc__' to see what is the documentation of that(current) class.

print(Student.__doc__)

# To check the documentation of the class you can also use the 'help' function.

print(help(Student))