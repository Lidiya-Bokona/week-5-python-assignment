class Car:
    def move(self):
        print("Driving 🚗")
class Bicycle:
    def move(self):
        print("Pedaling 🚲")
class Plane:
    def move(self):
        print("Flying ✈️")
vehicles = [Car(), Bicycle(), Plane()]
for vehicle in vehicles:
    vehicle.move()