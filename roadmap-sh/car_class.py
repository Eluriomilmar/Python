class Car:
    def __init__(self, model, year, color, for_sale):
        self.model = model
        self.year = year
        self.color = color
        self.for_sale = for_sale
        self.gas = 100

    def drive(self):
        print(f"Driving the {self.color} {self.model}... ")
        self.gas -= 1

    def stop(self):
        print(f"Stopped the {self.color} {self.model}.")

    def describe(self):
        print(f"{self.year} {self.model}  {self.color}")

    def refuel(self):
        self.gas = 100
        print(f"Gas tank has been refueled, it is now {self.gas}% full")