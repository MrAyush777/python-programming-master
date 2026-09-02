# Method overloading : is a concept where we can create a method that can be called in different ways.
# In Python, traditional method overloading (like in Java, C++, or C#) — where you can define multiple methods with the same name but different parameter lists — is not supported.
# If you define a method multiple times in the same class, the last definition will override the previous ones.
# So basically the method overloading is not suppported in python 

class A:
    def add(self,num1,num2):
        return num1 + num2
    
    # add method has overrided
    def add(self,num1,num2,num3):
        return num1 + num2 + num3
    
    
obj = A() 
# print(obj.add(10,20)) this will give an error. 

print(obj.add(10,20,30))
