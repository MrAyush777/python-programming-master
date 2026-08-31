# Instance Method : Any method that you created inside the class is called instance method.
# These are bound to the class not the instance
# To create a class method, we use a decorator -> classmethod

class Welcome:
    
# Below is a instance method. All methods defined inside the class are by default are instance methods.
    # def greet(self):
    #     print("Hello",self)

    collegeName = "Sal College"
    branches = ["BCA","MCA","B.Tech"]

# you can use either object or class to fetch class variables. like below :
    
    # 1) using class :
    @classmethod
    def greet(cls): # we will get class in the first argument of a class method. instead of 'self' here we will use 'cls' as a default argument because it is conventional(It means we can put any name as an argument but 'cls' is prefered.).
        print("Hello")
        print(cls)
        # using class :
        print(f"welcome to {cls.collegeName}")
        
    # 2) using object :
    def sports(self,sportsName):
        print(f"The student plays {sportsName} in the {self.collegeName} college")
        
    
    @classmethod
    def getBranches(cls):

        # it will give an error -> NameError : name 'branches' is not defined. use
        # for dpt in branches:
        #     print(dpt)
        
        for dpt in cls.branches:
            print(dpt)
        
        
gt1 = Welcome() # o/p : <cl ass '__main__.Welcome'>
gt1.greet()
print(Welcome) # <class '__main__.Welcome'>
# if it was object method than it will print like this : o/p -> <__main__.Welcome object at 0x000001F966797230>

gt1.sports("Cricket")
gt1.getBranches()
# help(Welcome)
