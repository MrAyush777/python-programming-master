# __init__() method : It is a special method in python classes that gets automatically called 
# It is an instance method used to create and intitialize the attributes during the object creation.
# init method get called automatically by python , implicitly or by default, whenever we create the object of that class. if you create 5 objects of that class, then this '__init__()' method will called 5 times automatically.

class Student:
    
    # def __init__(self):
    #     print("calling the initializer...")

# If you make second init method the python will override that method as we can see in the terminal(run python code)

# so ideally all the attributes or the variable should be defined inside the init method only.
    def __init__(self,name,roll_no,department):
        print(f"calling the initializer for {self}") 
        self.Name = name  # student.Name = "Ayush" / "Nehal"
        self.Roll_No = roll_no  # student.Roll_No = 12 / 10
        self.Department = department
        print(self.Name, self.Roll_No, self.Department)
    
    def sports(self,sport_name):  
        print(f"The student plays {sport_name}")
        
    def study(self,n_hours):
        print(f"The student {n_hours}")

student1 = Student("Ayush",12,"MCA")
student2 = Student("Nehal",10,"BCA")

print("===============================")
# in these parenthesis below, these are instance variables. like, student1.Name, student2.Roll_no, etc.
print(student1.Name, student1.Roll_No,student1.Department)
print(student2.Name,student2.Roll_No,student2.Department)
print("===============================")
print(student1.__dict__)
print(student2.__dict__)
print("===============================")
print(student1.__init__)
print(student2.__init__)
print("===============================")

# we defined instance variables inside the __init__ method of that class and initialize them values by creating their objects.     But we also can do this manually if we want extra argument later in the class like below :

student1.grade = "B"
# To check this use dict 
print(student1.__dict__)
print(student2.__dict__)
# as we can see that the student1 has 4 attributes and student2 has 3 attributes only. so that's it all.