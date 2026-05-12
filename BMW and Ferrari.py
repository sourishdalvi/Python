class BMW:
    def speed(self):
        print("BMW runs at 250 km/h")
    def fuel_type(self):
        print("BMW uses Petrol")
class Ferrari:
    def speed(self):
        print("Ferrari runs at 340 km/h")
    def fuel_type(self):
        print("Ferrari uses Premium Petrol")
def car_details(car):
    car.speed()
    car.fuel_type()
b = BMW()
f = Ferrari()
car_details(b)
print()
car_details(f)