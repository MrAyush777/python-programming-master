# Method overriding :   In Python, overriding allows a child class to provide a new implementation for a method already defined in its parent class. 
# Method overriding occurs when a child class defines a method with the same name as a method in its parent class. This allows the child class to provide its own implementation while retaining the inheritance relationship. It is commonly used to customize or extend the behavior of inherited methods.

class Employee:
    def working_hours(self): 
        return 45
    
class Intern(Employee):
    def working_hours(self):
        return 30

Intern1 = Intern()
print(Intern1.working_hours())