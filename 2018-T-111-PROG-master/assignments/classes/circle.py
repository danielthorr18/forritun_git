from math import pi


class Circle:
    def __init__(self, radius):
        self.__radius = float(radius)

    def __str__(self):
        return "Area: {:.2f}\nPerimeter: {:.2f}".format(self.area(), self.perimeter())

    def set_radius(self, new_radius):
        self.__radius = new_radius

    def get_radius(self):
        return self.__radius

    def area(self):
        return pi * self.__radius**2

    def perimeter(self):
        return 2 * pi * self.__radius
