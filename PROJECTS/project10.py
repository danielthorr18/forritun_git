class Vehicle:
    def __init__(self, the_license="", the_year=0, weight=0.0, fee=0.0):
        self.the_license = the_license
        self.the_year = the_year
        self.weight = weight
        self.fee = fee

    def get_year(self):
        return self.the_year
    
    def get_license(self):
        return self.the_license

    def get_weight(self):
        return self.weight
    
    def get_fee(self):
        return self.fee

    def __str__(self):
        return "Vehicle: {} {} Weight={:.2f} Fee=${:.2f}".format(self.the_license, self.the_year, self.weight, self.fee)


############################################################################################

class Car(Vehicle):
    def __init__(self, the_license, the_year, style="", weight=0.0, fee=0.0):
        Vehicle.__init__(self, the_license, the_year, weight, fee)
        self.style = style
    
    
    def set_weight(self, new_weight):
        self.weight = new_weight
        if self.weight == 0.0:
            fee = 0.0
        elif self.weight < 3000:
            fee = 30
        elif 3000 <= self.weight < 5000:
            fee = 40
        else:
            fee = 50
        self.fee = fee
        return self.fee
    
    def __str__(self):
        return "Car: {} {} {} Weight={:.2f} Fee=${:.2f}".format(self.the_license, self.the_year, self.style, self.weight, self.fee)

############################################################################################

class Truck(Vehicle):
    def __init__(self, the_license, the_year, wheels=0, weight=0.0, fee=0.0):
        Vehicle.__init__(self, the_license, the_year, weight, fee)
        self.wheels = wheels
    
    def set_weight(self, truck_weight):
        self.weight = truck_weight
        if self.weight < 3000:
            fee = 40
        elif 3000 <= self.weight < 5000:
            fee = 50
        elif 5000 <= self.weight < 10000:
            fee = 60
        else:
            fee = 70
        self.fee = fee
        return self.fee
    
    def __str__(self):
        return "Truck: {} {} {} wheels Weight={:.2f} Fee=${:.2f}".format(self.the_license, self.the_year, self.wheels, self.weight, self.fee)

############################################################################################

class Motorbike(Vehicle):
    def __init__(self, the_license, the_year, cc=0, weight=0.0, fee=0.0):
        Vehicle.__init__(self, the_license, the_year, weight, fee)
        self.cc = cc
    
    def get_CC(self):
        return self.cc

    def set_CC(self, new_cc):
        if new_cc < 50:
            fee = 10
        elif 50 <= new_cc < 200:
            fee = 20
        else:
            fee = 35
        self.fee = fee
        self.cc = new_cc
        return self.fee

    def __str__(self):
        return "Motorbike: {} {} {} cc Fee=${:.2f}".format(self.the_license, self.the_year, self.cc, self.fee)
    


def main():
    v1 = Vehicle("AB 123", 2010)
    c1 = Car("SF 735", 2007, "Station")
    t1 = Truck("TU 765", 1994, 6)
    b1 = Motorbike("XY 666", 2005)

    c1.set_weight(3500)
    t1.set_weight(9000)
    b1.set_CC(250)

    print(v1)
    print(c1)
    print("The weight of the car is: {:.2f}".format(c1.get_weight() ))
    print(t1)
    print("The fee for the truck is: {:.2f}".format(t1.get_fee() ))
    print(b1)
    print("The CC of the bike is: {:.2f}".format(b1.get_CC() ))
    print()

    vehicle_list = [v1, c1, t1, b1]
    for i in vehicle_list:
        print(i)
    v1 = c1
    print(v1)
    print()
main()