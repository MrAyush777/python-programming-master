# attribures can be either defined in the class or directly assigned to the object of that class.

class Student:
    pass

s1 = Student()
s2 = Student()

# here we defined attributes manually
s1.name = "Ayush"
s1.roll = 12

print(s1.name,s1.roll)
# print(s2.name,s2.roll) # it will give you an error : 'Student' object has no attribute 'name'

# dunder dict : it is something that can be used with objects to fetch the dictionary of the variables/attributes that are associated with a object. 
print(s1.__dict__) # It will return the dictionary. In that dictionary the key will be the variable name as a string and the value is it's corresponding value.
print(s2.__dict__) # It returns an empty string. Because we haven't make any attributes

