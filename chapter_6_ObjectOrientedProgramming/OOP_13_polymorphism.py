# polymorphism : one name different forms.
# help(int) # every operator has its own dunder method.

# Operator Overloading :

a = 5
b = 10 
# here a and b are two different objects of int class. And the + operator is overloaded for int class. So when we use + operator with two int objects, it will call the __add__ method of int class. So here a + b is actually calling a.__add__(b) method of int class.
print(a+b) # 15 <- externally we write like this  |  a.__add__(b) => int.__add__(a,b) <- internally it is calling like this.
print(a.__add__(b)) # 15 <- internally it is calling like this. 

str1 = "Hello"
str2 = " world"

class A:
    def f1(self, val):
        pass
    
obj = A()
A.f1(obj, 20)

class Rectangle:
    def __init__(self,length,breadth):
        self.Length = length
        self.Breadth = breadth
        
    def area(self):
        return self.Length * self.Breadth


    def __add__(self,other):
        return self.Length + other.Length  # r1.length + r1.length  | 10 + 5
                    
r1 = Rectangle(10,20)
r2 = Rectangle(5,7)
print(r1.area())
print(r2.area())

# print(r1 + r2) # it will give error because + operator is not overloaded for Rectangle class.so we need to overload the + operator for Rectangle class. To do that we need to define the __add__ method in Rectangle class. So when we use + operator with two Rectangle objects, it will call the __add__ method of Rectangle class. So here r1 + r2 is actually calling r1.__add__(r2) method of Rectangle class.
# Error : TypeError: unsupported operand type(s) for +: 'Rectangle' and 'Rectangle'
# In the case of integers(a and b) and strings(str1 and str2),  they both have dunder add method(__add__()), thats why the + operator has overloaded or worked.
# But in the case of r1 and r2, these are obects of Rectangle class. And Rectangle class doesn't have any dunder method like + (__add__). So it will give you an error. 

# so any user defined or builtin classes, if they do not have dunder add method defined in it, you cannot use the plus operator with that particular class or that object of that particular class.  

# now when we have __add__ method :
print("dunder",r1 + r2) # now internall it will work like this : Rectangle.__add__(r1,r2)
# here r1 will go to 'self' and r2 will go to 'other'



# So it overloading btw...