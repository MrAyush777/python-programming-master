# Abstract Class and Abstract mehthod : 
# Below : To use area() mehtod of the shape class, make sure that classes of this class will inherit the shape class.

from OOP_18_myAbstractBaseClass import Shape

class Square(Shape):

    def __init__(self,side):
        self.Side = side
    
    def area(self):
        return self.Side ** 2 


class Rectangle(Shape):

    def __init__(self,length,breadth):
        self.Length = length
        self.Breadth = breadth
        
    def area(self):
        return self.Length * self.Breadth 


class Circle(Shape):
    
    def __init__(self,radius):
        self.Radius = radius
        
    def area(self):
        return 3.14 * self.Radius ** 2
        


sq1 = Square(10)
print(sq1.area())   

r1 = Rectangle(10,15)
print(r1.area())



c1 = Circle(10) # without implementation of area method in circle class, it will give you an error like below :
# TypeError: Can't instantiate abstract class Circle without an implementation for abstract method 'area'
# It means it doesn't allows you to create an object of cirlle class because, you have not implemented the area() method
# Here is mean to say : abstract class(Shape) forces the circle class to basically have the area method now. 
# In other words, abstract class is kind of a framework that the child class() should follow. 
# The child class should follow any class that is inheriting the abstract class, that child class should basically follow and should have the abstract methods defined in it.

print(c1.area())
# ==============================================================================================

# to create Abstract class we need to import ABC(Abstract Base Class) and decorator called 'abstractmethod'
# It means from the 'abc' module we are going to import class namede 'ABC' 
# 'abstractmethod' decorator helps us to create abstract methods  
# below abc is a module and ABC is a class of that module, which is a parent or root class we can say.

# In Python, an abstract method is a method that is declared in an abstract base class (ABC) but has no implementation in that class.
# It acts as a blueprint — any subclass must provide its own implementation of the method.

