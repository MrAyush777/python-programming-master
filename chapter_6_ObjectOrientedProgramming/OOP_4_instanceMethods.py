# objects are called instance of the class.
# Instance method is a method that defined inside a class which is bound to/associated with the instance/object.

# help(list)
# l1 = [10,20,30] # Here l1 is an object of 'list' class.

class Student:
    """
    This class is used to manage activities and infomation of the student.
    """
    
    # def study():  # This is an instance method. 
    #     print("The student studies for 3 hours a day.")
        
# student1 = Student()
# print(student1) # It will return a memory address of this object, where this object has created.
# student1.study()

# It can also be with function like below :

# def greet():
#     print("Hello World...")
    
# greet("python") # It will generate same error.

# =========================================================

# but in the case of method. We haven't entered any argument when calling the method, still it give us the same error.
# It is because, when we haven't specify any argument inside the method while calling it, something gets passed automatically or internally by python.   
# To solve this problem just write anything inside the function, without the double quotes. and it will work.

    def study(args): # here args is not a keyword, it's user defined...
        print("The Ayush is very honest person i have ever seen.")

    def study2(self):
        print(f"The self is : {self}") # Output : the memory address of this class's object and the memeory address of 'self' is same. That is the proof that the object itself is getting passsed as the first argument here.

    def study3(self,n_hours):
        print(f"self is : {self}")
        print(f"The student studied for {n_hours} hours a day !")

    def sports(self,sports_name):
        print(f"self is {self}")
        print(f"Student plays {sports_name}")
    
student2 = Student()
print(student2)
student2.study()
student2.study2() 

"""
Now let's find what python automatically pass something when we call any instance method of the class using the object/instance of the class,
Python passes the object itself as the first argument.
============ The first argument is by standard is 'self' ============   
It means we can write self inside that method. That is a standard of the python.
"""

# So in our case the python will pass student1 object inside the study mehtod , internally and automatically.

# now let's know about 'self' :

# help(list) # when you run this, the terminal shows all methods and uses of list. If you notice, these methods are pass 'self' as the first argument in the method.
# for example look at the append function from the list.
# It proves that even the built-in classes or the built-in data types have self as the first argument of the instance method 
# See 'append()' functino also takes another argument which is any object or any value that needs to be added to the existing list.

# let's understand it with an example : 

print("-------------------------------------------------------------------")

student3 = Student()
print(f"The object : {student3}")
student3.study3(3)

print("-------------------------------------------------------------------")

student4 = Student()
print(f"The object : {student4}")
student4.study3(4)

print("-------------------------------------------------------------------")

student2.sports("Football")