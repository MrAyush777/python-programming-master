# static method : method defined inside a class which is neither bound to the object nor to the class
# To create a static method, we use staticmethod decorator
# no argument will pass by default in the static method.(it's not like class(cls) and init method(self))


class Student:
    
    @staticmethod
    def greet():
        print("Hello, python!")
        

student_1 = Student()
student_1.greet()

help(Student)