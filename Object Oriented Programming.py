# Utilizing Polymorphism to group smaller object classes into larger one for Shapes
class Shape:
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        return self.base * self.height

    def perimeter(self):
        return (self.base * 2) + (self.height * 2)

#Creating the square shape class to determine length/perimeter
class Square(Shape):
    def __init__(self, length):
        super().__init__(length, length)

#Creating the triangle shape class to determine length/perimeter
class Triangle(Shape):
    def __init__(self, base, height, side1, side2, side3):
        super().__init__(base, height)
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3

#Overided parent class area/perimeter functions with unique ones
    def area(self):
        return (self.base * self.height) / 2

    def perimeter(self):
        return self.side1 + self.side2 + self.side3

#Creating the Rectangle shape class to determine length/perimeter
class Rectangle(Shape):
    def __init__(self, base, height):
        super().__init__(base, height)

#Now that all shapes are in one class, can create a list of them and condense code
listOfShapes = [Square(4), Triangle(4, 5, 10, 20, 40), Rectangle(8, 19)]
for shape in listOfShapes:
    print(shape.area(), shape.perimeter())

