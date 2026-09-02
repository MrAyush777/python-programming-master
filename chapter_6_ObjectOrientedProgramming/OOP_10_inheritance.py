class Vehicle:
    company = "Honda"
    
    def __init__(self,n_wheels, n_seats, mileage):
        print("init of vehicle :\n")
        self.nWheels = n_wheels
        self.nSeats = n_seats
        self.mileAge = mileage
        
    def getDetails(self):
        return f"This vehicle has {self.nWheels} wheels, {self.nSeats} seats and provides mileage of {self.mileAge} km/litre."
    
    
v1 = Vehicle(4,5,15)
print(v1.getDetails())

# Now let's see how inheritance works in python

# below Vehicle class is inherited by Car class

class Car(Vehicle):
    # pass # when there is no init method in child class , the init method of parent class gets called, when you create an object of child class
    
    model = "swift"
    print("init of car :\n")

    # def __init__(self,car_type,drive_type):
    def __init__(self,car_type,drive_type,wheels,seats,mileage):
        self.carType = car_type
        self.driveType = drive_type
        # Vehicle.__init__(4,7,15) # this will give an error that : require one positional argument: 'mileage'
        # self.__init__(4,7,15) # this will also give an error that : takes 3 positional arguments but 4 were given. To solve this just write 'self' as a first argument, like below :
        # Vehicle.__init__(self,4,7,15)
        
        # super().__init__(4,7,15) # when you use super, it will actually refer to the parent class(Vehicle class) and when you use super, you not need to pass 'self' as a first agrument explicitly. super will take care of passing self as the first argument. so don't pass 'self' when call the method otherwise it will give an error.
        # parent class is also called the super class
        
        # here by using super() method, we basically hard code the values and pass them. Instead of doing that we can take these arguments from the object(while creating object of that class itself)
        # to do that simplly pass that arguments inside the init method of child class(Car class). See init method of the child class(Car class) and the write like below :

        super().__init__(wheels,seats,mileage)
        
                
# car class is called child/sub/derived class
# vehhicle class is called parent/super/base class

# c1 = Car() # it will give error because we have not passed the required arguments in the constructor of Vehicls class. So we need to pass the required arguments in the constructor of Car class as well. Because Car class is inheriting the constructor of Vehicle class.
# c1 = Car(4,5,15)
# print(c1)

# we also can retrieve the attributes of parent class using child class object (c1 here)
# print("mileage : ",c1.mileAge)"
# print("number of wheels : ",c1.nWheels)
# print("number of seats : ",c1.nSeats)

# we also can retrieve the class varible of parent class using child class object (c1 here is child class object)
# print("company : ",c1.company)
# print(c1.getDetails())


c2 = Car("SUV","Manual",4,7,20)
print(c2)
print(c2.model)
print(c2.company)
print(c2.mileAge) # it will give error. Because it is calling the init mithod of the car class not the vehicle class. because the car class has its own init method.You have to explicitely call the inti method of the parent class(Vehicle) in the child class(Car)  
# To do that just call init method of the parent class inside the init mehtod of the child class(Car).

print(c2.getDetails())
print(c2.__dict__)  # it will give you all instance level variable/attributes of the object

print()

# c3 = Car("SUV","Manual",4,7,20)

# There is another method of initialze the init of parent class by using 'super() method' : See initializer method of the car class. 



# help(Car)