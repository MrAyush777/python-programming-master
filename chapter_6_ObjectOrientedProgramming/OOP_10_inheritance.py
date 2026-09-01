class Vehicle:
    company = "Honda"
    
    def __init__(self,n_wheels, n_seats, mileage):
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
    pass
# car class is called child/sub/derived class
# vehhicle class is called parent/super/base class


# c1 = Car() # it will give error because we have not passed the required arguments in the constructor of Vehicls class. So we need to pass the required arguments in the constructor of Car class as well. Because Car class is inheriting the constructor of Vehicle class.
