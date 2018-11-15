# Implement the class Circle which has a private member variable for radius. 
# Implement the member functions needed for the following program to run:
# def main():   
#     radius = input("Radius of circle: ")        
#     circle = Circle(radius)
#     print(circle)
#     circle.set_radius(circle.get_radius() + 1.0)   
#     print(circle)
# main()
# You will need to use the constant PI = 3.14159 in your  program. Find out how to use it from the math module.
# Example if the main function above is run : (Note that 3.0 is the input from the user)
# Radius of circle: 3.0
# Area: 28.27
# Perimeter: 18.85
# Area: 50.27
# Perimeter: 25.13
# You should only hand in the code for the class

import math

class Circle:
    def __init__(self, radius):
        self.__radius = float(radius)
    
    def __str__(self):
        return "Area: {:.2f}\nPerimeter: {:.2f}".format(self.area(), self.perimeter()) #float m 2 aukastofum
    
    def area(self): #flatarmal
        return math.pi * self.__radius**2 #radius i odru sinnum pi 
    
    def perimeter(self): #ummal
        return 2*math.pi * self.__radius
    
    def set_radius(self, new_radius):
        self.__radius = new_radius        
    
    def get_radius(self):
        return self.__radius


def main():   
    radius = input("Radius of circle: ")        
    circle = Circle(radius)
    print(circle)
    circle.set_radius(circle.get_radius() + 1.0)   
    print(circle)

main()