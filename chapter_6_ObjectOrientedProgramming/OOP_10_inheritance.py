class Vehicle:
    company = "Honda"
    
    def __init__(self,n_wheels, n_seats, mileage):
        self.nWheels = n_wheels
        self.nSeats = n_seats
        self.mileAge = mileage
        
    def getDetails(self):
        return f"This vehicle has {self.nWheels}, {self.nSeats} and provides mileage of {self.mileAge} km/litre."
    
    
v1 = Vehicle(4,5,15)
print(v1.getDetails())