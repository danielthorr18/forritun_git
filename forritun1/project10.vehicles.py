class Vehicle:
  def init(self, the_license, the_year):
    self.the_license = the_license 
    self.the_year = the_year 

  def get_license(self):
    pass

  def get_year(self):
    pass

  def get_weight(self):
    pass

  def set_weight(self, weight):
    self.weight = weight

  def get_fee(self, fee):
    self.fee = fee

  def set_fee(self):
    pass

  def str(self):
    pass

class Car(Vehicle):

  def init(self, the_license, the_year, the_style):
    Vehicle.init(self, the_license, the_year)
    self.the_license = the_license 
    self.the_year = the_year 
    self.the_style = the_style 

  def set_weight(self, weight):
    self.weight = weight

  def set_fee(self, weight):
    if self.weight < 3000:
      self.fee = 30
    elif self.weight >= 3000 and self.weight < 5000:
      self.fee = 40
    else:
      self.fee = 50


  def str(self):
    return "Car: {} {} {} Weight={} Fee=${}".format(self.the_license,self.the_year,self.the_style,self.weight, self.fee)
class Truck(Vehicle):
  def init(self, the_license, the_year, the_wheels):
    Vehicle.init(self, the_license, the_year)
    self.the_license = the_license
    self.the_year = the_year
    self.the_wheels = the_wheels

  def set_weight(self, weight):
    self.weight = weight

  def set_fee(self):
    if self.weight < 3000:
      self.fee = 40
    elif self.weight >= 3000 and self.weight < 5000:
      self.fee = 50
    else:
      self.fee = 70
    return self.fee

  def str(self):
    return "Truck: {} {} {} wheels Weight={} Fee=${}".format(self.the_license,self.the_year,self.the_wheels,self.weight, self.fee)

class Motorbike(Vehicle):

  def init(self, the_license, the_year):
    Vehicle.init(self, the_license, the_year)
    self.the_license = the_license
    self.the_year = the_year

  def get_CC(self):
    pass

  def set_CC(self, CC):
    self.CC = CC
    if self.CC < 50:
      self.fee = 10
    elif self.CC >= 50 and self.CC < 200:
      self.fee = 20
    else:
      self.fee = 35
    return self.CC

  def str(self):
    return "Motorbike: {} {} {} cc Fee=${}".format(self.the_license,self.the_year,self.CC, self.fee)