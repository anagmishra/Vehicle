class Vehicle:
    def __init__(self, brand, speed):
        self.brand = brand
        self.speed = speed

    def desc(self):
        print(f"This is a {self.brand} vehicle moving at {self.speed} km/h.")

class Car(Vehicle):
    def __init__(self, brand, speed, fuel_type):
        super().__init__(brand)
        super().__init__(speed)
        self.fuel_type = fuel_type
    
    def output(self):
        print(f"This is a {self.brand} car running on {self.fuel_type} moving at {self.speed} km/h.")

Car1 = Car("Chevorlet", 100, "petrol")
Car1.desc()
Car1.output()
