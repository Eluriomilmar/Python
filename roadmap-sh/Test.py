import shapes_class

shapes = [shapes_class.Circle(4), shapes_class.Square(5), shapes_class.Triangle(6,7), shapes_class.Pizza("Pepperoni", 15)]

for shape in shapes:
    print(shape.area())