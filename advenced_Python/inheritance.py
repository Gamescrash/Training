class Vehicle:
    def general_usage(self):
        print("general use: transportation")

class Car(Vehicle):
    def __init__(self):
        print("I'm car")
        self.wheels = 4
        self.has_roof = True

    def specific_usage(self):
        self.general_usage()
        print("is spacious and protective")

class Motorcycle(Vehicle):
    def __init__(self):
        print("I'm motor cycle")
        self.wheels = 2
        self.has_roof = False

    def specific_usage(self):
        self.general_usage()
        print("is fast and cool")


c = Car()
c.specific_usage()

m = Motorcycle()
m.specific_usage()

print(isinstance(c, Car))
print(issubclass(Car,Vehicle))