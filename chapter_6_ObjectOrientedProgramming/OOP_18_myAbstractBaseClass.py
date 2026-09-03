# to create Abstract class we need to import ABC(Abstract Base Class) and decorator called 'abstractmethod'
# It means from the 'abc' module we are going to import class namede 'ABC' 
# 'abstractmethod' decorator helps us to create abstract methods  
# below abc is a module and ABC is a class of that module, which is a parent or root class we can say.

# In Python, an abstract method is a method that is declared in an abstract base class (ABC) but has no implementation in that class.
# It acts as a blueprint — any subclass must provide its own implementation of the method.


from abc import ABC, abstractmethod

class Shape(ABC):
    
    @abstractmethod
    def area(self):
        pass