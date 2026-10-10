
class Vehicle:

    def __init__(self, brand, max_speed):
        self.brand = brand
        self.max_speed = max_speed

    def show_details(self):
        print("Brand:", self.brand)
        print("Maximum Speed:", self.max_speed, "km/h")


class Car(Vehicle):

    def __init__(self, brand, max_speed, model, seats):
        super().__init__(brand, max_speed)
        self.model = model
        self.seats = seats

    def show_details(self):
        print("Model:", self.model)
        print("Seats:", self.seats)
        super().show_details()

    def fuel_type(self):
        print("Fuel Type: Petrol")


my_car = Car("Mercedes-Benz", 250, "C-Class", 5)

my_car.show_details()
my_car.fuel_type()

print("Is Car a subclass of Vehicle?", issubclass(Car, Vehicle))