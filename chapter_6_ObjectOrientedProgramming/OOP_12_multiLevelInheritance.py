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

class Car(Vehicle):

    model = "swift"
    print("init of car :\n")

    def __init__(self,car_type,drive_type,wheels,seats,mileage):
        self.carType = car_type
        self.driveType = drive_type
        super().__init__(wheels,seats,mileage)

    def get_details(self):
        print(f"car type : {self.carType}, drive type : {self.driveType} ")

c2 = Car("SUV","Manual",4,7,20)
print(c2)
print(c2.model)
print(c2.company)
print(c2.mileAge) 
print(c2.getDetails())
print(c2.__dict__) 


class ElectricCar(Car):
    
    def __init__(self,car_type,drive_type,wheels,seats,mileage,battery_capacity,distance_range):
        print("init of Electric Car")
        self.batteryCapacity = battery_capacity
        self.distanceRange = distance_range
        super().__init__(car_type,drive_type,wheels,seats,mileage)
        
    def charge(self):
        print(f"charging the car to {self.batteryCapacity}")
    
    
ec1 = ElectricCar("Sedan","Manual",4,5,35,100,400)
print("object ec1 details :\n",ec1.__dict__)

help(ElectricCar)