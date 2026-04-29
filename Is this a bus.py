class Vehicle:
    def __init__(self, make, max_speed,mileage):
        self.make = make
        self.max_speed = max_speed
        self.mileage = mileage
class Bus(Vehicle):
 pass
School_bus = Bus("School Volvo", 180, 12)
print("Vehicle Name:", School_bus.make, "Speed:", School_bus.max_speed, "Mileage:", School_bus.mileage)
