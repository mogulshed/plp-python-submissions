# Assignment 1: Design Your Own Class 🏗️
class Smartphone:
    def __init__(self, brand, model, price):
        self.brand = brand
        self.model = model
        self.price = price  

    def phone_info(self):
        return f"{self.brand} {self.model}, Price: ${self.price}"

    def make_call(self, number):
        return f"Calling {number} from {self.model}..."

# Inheritance example
class GamingSmartphone(Smartphone):
    def __init__(self, brand, model, price, gpu):
        super().__init__(brand, model, price)
        self.gpu = gpu

    def phone_info(self):  # overriding method
        return f"{self.brand} {self.model} (Gaming, GPU: {self.gpu}), Price: ${self.price}"


# Activity 2: Polymorphism Challenge 

class Car:
    def move(self):
        return "Driving 🚗"

class Plane:
    def move(self):
        return "Flying ✈️"


# Testing Deliverables
if __name__ == "__main__":
    # Assignment 1 test
    phone1 = Smartphone("Samsung", "Galaxy S23", 1200)
    phone2 = GamingSmartphone("Asus", "ROG 7", 1500, "Adreno 740")

    print(phone1.phone_info())
    print(phone1.make_call("+123456789"))
    print(phone2.phone_info())

    # Activity 2 test
    print("\n--- Polymorphism Demo ---")
    vehicles = [Car(), Plane()]
    for v in vehicles:
        print(v.move())
