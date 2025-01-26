# Assignment 1: Design Your Own Class - Smartphone

class Smartphone:
    def __init__(self, brand, model, storage, price):
        self.brand = brand
        self.model = model
        self.storage = storage
        self.price = price

    def call(self, number):
        return f"Dialing {number} from {self.model}..."

    def browse(self):
        return f"Browsing the internet on {self.model}."

class Smartwatch(Smartphone):
    def __init__(self, brand, model, storage, price, strap_material):
        super().__init__(brand, model, storage, price)
        self.strap_material = strap_material

    def track_health(self):
        return f"Tracking health metrics on {self.model} with a {self.strap_material} strap."

# Example Usage
smartphone = Smartphone("Samsung", "Galaxy A16", "128GB", 1200)
print(smartphone.call("+254743714202"))
print(smartphone.browse())

smartwatch = Smartwatch("Apple", "Watch Series", "32GB", 500, "silicone")
print(smartwatch.call("+254743714202"))
print(smartwatch.track_health())

# Activity 2: Polymorphism Challenge - Vehicles

class Vehicle:
    def move(self):
        raise NotImplementedError("Subclasses must implement this method")

class Car(Vehicle):
    def move(self):
        return "Driving on the road 🚗"

class Plane(Vehicle):
    def move(self):
        return "Flying in the sky ✈️"

class Boat(Vehicle):
    def move(self):
        return "Sailing on the water 🚤"

# Example Usage
vehicles = [Car(), Plane(), Boat()]
for vehicle in vehicles:
    print(vehicle.move())
