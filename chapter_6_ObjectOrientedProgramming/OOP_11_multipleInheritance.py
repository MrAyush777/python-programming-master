# Multi level inheritance :

class A:
    def state_1(self):
        print("State 1 present")    
    def state_2(self):
        print("State 2 present")    
    def state_3(self):
        print("State 2 present")    
    
class B:
    def state_4(self):
        print("State 4 present")
    def state_5(self):
        print("State 5 present")
    
# Multiple Inheritance : A class can inherit from multiple classes. In this case, the child class will have access to all the methods and attributes of the parent classes.
class C(A,B):
    def state_6(self):
        print("State 6 present")


c = C()
c.state_1()
c.state_2()
c.state_3()
c.state_4()
c.state_5()

# As we can see that the object of the child class C has acces to all the methods of the parent classes A and B. This is called multiple inheritance.