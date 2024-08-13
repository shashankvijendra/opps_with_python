class Vehicle:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

    def start_engine(self):
        print(f"The {self.brand} {self.model}'s engine starts.")

    def stop_engine(self):
        print(f"The {self.brand} {self.model}'s engine stops.")


class Car(Vehicle):
    def __init__(self, brand, model, year, color):
        super().__init__(brand, model, year)
        self.color = color

    def honk(self):
        print(f"The {self.color} {self.model} says: Honk!")

class Motorcycle(Vehicle):
    def __init__(self, brand, model, year, type):
        super().__init__(brand, model, year)
        self.type = type  # Type could be sport, cruiser, etc.

    def wheelie(self):
        print(f"This {self.type} motorcycle does a wheelie!")


my_car = Car("Toyota", "Corolla", 2020, "Blue")
my_motorcycle = Motorcycle("Harley-Davidson", "Street 750", 2018, "cruiser")

my_car.start_engine()
my_car.stop_engine()
my_car.honk()

my_motorcycle.start_engine()
my_motorcycle.stop_engine()
my_motorcycle.wheelie()
