"""
object = a container
which contains 2 things : data and functionality    

1) data = attributes 
2) functionality = methods/behaviour
"""

# To understand this concept let't take one example here :

fruits = ["mango","banana","pinapple"]
print(type(fruits)) # output : <class : 'list'>

# here list is a class and fruits is the object of that(list's) class.
# here 'fruits' is a container that stores some data like, mango,banana,pinapple, etc. and list is a class of that object.

""" second real world example :

car1 =     ----> it is a container    
    => brand = "BMW", model = "XYZ234" year = 2026    ----> these are data/attributes
    => brake, playMusic, accelerate   ----> these are methods/behaviours/functionality
"""

"""
To access these data and behaviours. The '.' operator is used like below :

car1.brand
car1.model
car1.brake() 
car1.playMusic()
"""

"""
creating objects :

we need a car to create an object. 
"""

# =================================================================================================================

# classes => templates/blueprints/design used for creating objects.
# also called a type

# objects are created using the class 
# objects are called instances of that class. 
# here The word 'instances' means 'example'. It means the Car1 is an example/type of a car. 

# ===================================================================================================================

# The functions that are defined inside a class is known as Methods. or we can say that any function that get's defined insed a class becomes automatically method of that class. 
# so that append method does not append the function.

class MyClass:
    pass # pass is a keyword that is used to make code syntactically correct. We can use this whenever we want to make an empty class.


# creating an object. Below obj1 and obj2 are objects of MyClass.    
obj1 = MyClass()
obj2 = MyClass()
l1 = [10,20,30]

print(type(l1)) # output : <class 'list'> 
print(type(obj1)) # output : <class '__main__.MyClass'>
print(type(obj2)) # output : <class '__main__.MyClass'>

# here anything starting and ending with double underscore is called 'Dunder'. D means Double and Under means Underscore. This is special method or have special meaning in python.

# Calling methods using objects : using '.' notations 
# syntax : object.method(arguments)