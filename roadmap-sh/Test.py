class Car:
    def __init__(self, model, year, color, for_sale):
        self.model = model
        self.year = year
        self.color = color
        self.for_sale = for_sale

car1 = Car("Fusca", "1980", "azul", True)
print(f"{car1.model}\n{car1.year}\n{car1.color}\n{car1.for_sale}")