# class variavles : 
# These are defined at the class level
# same copy of the class variables are shared amont all objects of the class

class Student:
    
    collegeName = "SAL College"
    departments = ["Arts","Commerce","Science"]
    
    def __init__(self,name,roll_no):
        print(f"\ncalling the initializer for {self}")
        print("I am iron man")
        self.Name = name
        self.Roll_No = roll_no

        print(self.Name,self.Roll_No)       
        
    def study(n_hours):
        print(f"i am study {n_hours} a day")
        

std1 = Student("Ayush",12)
std2 = Student("Mahi",14)
std3 = Student("Krunal",16) 

# help(Student) # see the section of "Data and other attributes defined here:" <<-- this will show your class variables. 
# In our class -> collegName and departments are class variable, which will share the same copy with all the objects of the student class.

print(std1.__dict__) # std1.__dict__ will only have instance variables, it will not show you the class variables

# We can access these class variables using class name or instancae names, like below :

# 1) using class name :
# print(Student.__dict__) # It will print all the details. Wrong approach
print(f"using class name : {Student.collegeName}")
print(f"using class name : {Student.departments}")


# 2) using instance name :
print(f"using instance name : {std1.collegeName}") # It will print the values of the class variables :
print(f"using instance name : {std1.departments}")
