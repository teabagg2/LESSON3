class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def display_info(self):
        print(f"Car: {self.year} {self.make} {self.model}")

    def top_speed(self, speed):
        print(f"Top speed of {self.make} {self.model} is {speed} km/h")


class Benz(Car):
    def __init__(self, make, model, year, luxury_level):
        super().__init__(make, model, year)
        self.luxury_level = luxury_level

    def display_info(self):
        print(f"Benz: {self.year} {self.make} {self.model}, Luxury Level: {self.luxury_level}")

    def top_speed(self, speed):
        print(f"Top speed of {self.make} {self.model} is {speed} km/h")


child = Benz("Mercedes-Benz", "C-Class", 2022, "High")

child.display_info()
child.top_speed(250)

         